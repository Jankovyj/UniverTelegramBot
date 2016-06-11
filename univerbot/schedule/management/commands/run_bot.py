from django.conf import settings
from django.core.management.base import BaseCommand

import time
import datetime
import subprocess
import telepot
import json


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

    def get_api_method(self, command):
        # TODO rewrite get_api_method(), when commands will be known
        # at first i should know which command we will used
        #
        # /all - all schedules for all groups
        # {pk} - schedules for group with pk=pk

        api_method = ''

        def is_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        if command == '/all':
            api_method = '/timetables/'
        elif is_int(command):
            api_method = '/timetables/{0}/'.format(command)

        return api_method

    def get_answer(self, api_method):
        string_request = 'http -a {0}:{1} {2}{3}'.format(settings.DRF_USERNAME, settings.DRF_PASSWORD,
                                                         settings.HOST, api_method)
        shell_request = subprocess.Popen(string_request, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        response = shell_request.stdout.read()

        timetables = json.loads(response.decode('utf-8'))

        # answer = self.generate_html_answer(timetables)
        answer = timetables

        return answer

    # def generate_html_answer(self, timetables):
    #     html_answer = ''
    #     week_days = ['Monday', 'Tuesday', 'Wednesday',
    #                  'Thursday', 'Friday', 'Saturday', 'Sunday']
    #
    #     # TODO rewrite generate_html_answer(), when style will be known
    #     # dont judge, its only for beginning ))
    #     for group_timetables in timetables:
    #         html_answer += '<b>Group: {0}</b>'.format(group_timetables['name'])
    #         for day, schedules in sorted(group_timetables['timetables'].items()):
    #             html_answer += '\n-<i>{0}</i>'.format(week_days[int(day) - 1])
    #             for key, schedule in schedules.items():
    #                 html_answer += '\nCabinet: {0}\nTeacher: {1}\
    #                         \nSubject: {2}\nTime: {3}\n'.format(schedule['cabinet'], schedule['teacher'],
    #                                                             schedule['subject'], schedule['time'])
    #         html_answer += '\n'
    #
    #     return html_answer

    def handle_msg(self, msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        api_method = self.get_api_method(command)
        answer = self.get_answer(api_method)

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
