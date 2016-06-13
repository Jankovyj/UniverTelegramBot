from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from department.models import Group

import time
import datetime
import subprocess
import telepot
import json
import re


class UniverTelegramBot:

    def __init__(self):
        self.bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
        self.bot.message_loop(self.handle_msg)

    def log(self, msg, answer):
        print('------')
        print(datetime.datetime.now())
        print('Send from {0} {1} (id = {2})\nText: {3}'.format(msg['from']['first_name'],
                                                               msg['from']['last_name'],
                                                               str(msg['from']['id']),
                                                               msg['text']))
        print(answer)

    def get_api_method_and_html_answer_template(self, command):
        # /tt all - all timetables for all groups
        # /tt {group_name} - timetables for group with name=group_name

        api_method = ''
        html_answer_template = 'error'

        command = re.search(r'^/tt\s(\w+)', command)
        if command:
            command = command.group(1)
            if command == 'all':
                api_method = '/timetables/'
                html_answer_template = 'all'
            else:
                try:
                    group_id = Group.objects.get(name__contains=command).id
                    api_method = '/timetables/{0}/'.format(group_id)
                    html_answer_template = 'with_group_id'
                except ObjectDoesNotExist:
                    html_answer_template = 'error'
                    print('ObjectDoesNotExist')

        return api_method, html_answer_template

    def get_answer(self, api_method, html_answer_template):
        string_request = 'http -a {0}:{1} {2}{3}'.format(settings.DRF_USERNAME, settings.DRF_PASSWORD,
                                                         settings.HOST, api_method)
        shell_request = subprocess.Popen(string_request, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        response = shell_request.stdout.read()

        timetables = json.loads(response.decode('utf-8'))

        answer = self.generate_html_answer(timetables, html_answer_template)

        return answer

    # TODO rewrite this method.
    def generate_html_answer(self, timetables, html_answer_template):
        html_answer = ''
        week_days = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']

        # yeah, yeah, i know, its only for test )
        if html_answer_template == 'all':
            for group_timetables in timetables:
                html_answer += '<b>Group: {0}</b>'.format(group_timetables['name'])
                for day, schedules in sorted(group_timetables['timetables'].items()):
                    html_answer += '\n-<i>{0}</i>'.format(week_days[int(day) - 1])
                    for key, schedule in schedules.items():
                        html_answer += '\nCabinet: {0}\nTeacher: {1}\
                                \nSubject: {2}\nTime: {3}\n'.format(schedule['cabinet'], schedule['teacher'],
                                                                    schedule['subject'], schedule['time'])
                html_answer += '\n'
        elif html_answer_template == 'with_group_id':
            html_answer += '<b>Group: {0}</b>'.format(timetables['name'])
            for day, schedules in sorted(timetables['timetables'].items()):
                html_answer += '\n-<i>{0}</i>'.format(week_days[int(day) - 1])
                for key, schedule in schedules.items():
                    html_answer += '\nCabinet: {0}\nTeacher: {1}\
                            \nSubject: {2}\nTime: {3}\n'.format(schedule['cabinet'], schedule['teacher'],
                                                                schedule['subject'], schedule['time'])
            html_answer += '\n'
        elif html_answer_template == 'error':
            html_answer += '<b>Invalid command</b>'

        return html_answer

    def handle_msg(self, msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        api_method, html_answer_template = self.get_api_method_and_html_answer_template(command)
        answer = self.get_answer(api_method, html_answer_template)

        self.log(msg, answer)
        self.bot.sendMessage(chat_id=chat_id, text=answer, parse_mode='HTML')


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # init bot
        UniverTelegramBot()

        print('Listening...')
        # keep program running
        while 1:
            time.sleep(10)