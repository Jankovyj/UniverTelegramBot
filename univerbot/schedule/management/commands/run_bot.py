from django.conf import settings
from django.core.management.base import BaseCommand

import time
import datetime
import subprocess
import telepot
import json


class Command(BaseCommand):

    bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)

    def log(self, msg, answer):
        print('------')
        print(datetime.datetime.now())
        print('Send from {0} {1} (id = {2})\nText: {3}'.format(msg['from']['first_name'],
                                                               msg['from']['last_name'],
                                                               str(msg['from']['id']),
                                                               msg['text']))
        print(answer)

    def get_answer(self, api_method):
        string_request = 'http -a {0}:{1} {2}{3}'.format(settings.DRF_USERNAME, settings.DRF_PASSWORD,
                                                         settings.HOST, api_method)
        shell_request = subprocess.Popen(string_request, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        response = shell_request.stdout.read()

        # TODO it will be normally parsed soon
        answer = json.loads(response.decode('utf-8'))

        return answer

    def handle_msg(self, msg):
        chat_id = msg['chat']['id']
        # command = msg['text']

        # TODO something like switch will be provided here
        api_method = '/timetables/'

        answer = self.get_answer(api_method)

        self.log(msg, answer)
        self.bot.sendMessage(chat_id, answer)

    def handle(self, *args, **kwargs):
        self.bot.message_loop(self.handle_msg)

        self.stdout.write('Listening...')
        # keep program running
        while 1:
            time.sleep(10)
