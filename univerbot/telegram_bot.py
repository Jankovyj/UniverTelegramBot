import time
import datetime
import subprocess
import telepot
import json

import codecs


TOKEN = '230745447:AAESNsepqjmi9bOKqv2AkEC3udtErWPD4WU'

# for getting permission to api
USERNAME = 'admin'
PASSWORD = 'b123456b'

HOST = 'http://0.0.0.0:8000'


def log(msg, answer):
    print('------')
    print(datetime.datetime.now())
    print('Send from {0} {1} (id = {2})\nText: {3}'.format(msg['from']['first_name'],
                                                           msg['from']['last_name'],
                                                           str(msg['from']['id']),
                                                           msg['text']))
    print(answer)


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    # TODO something like switch will be provided here
    api_method = '/timetables/'

    string_request = 'http -a {0}:{1} {2}{3}'.format(USERNAME, PASSWORD, HOST, api_method)
    shell_request = subprocess.Popen(string_request, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    response = shell_request.stdout.read()

    # TODO it will be normally parsed soon
    answer = json.loads(response.decode('utf-8'))

    log(msg, answer)
    bot.sendMessage(chat_id, answer)


bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Listening...')

# keep program running
while 1:
    time.sleep(10)
