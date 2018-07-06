#!/usr/bin/env python3
import requests
token="350328341:AAGMnO9TM1H88BgYEIjKeAZzsn0twBimi6U"
class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler(token)   

def main():  
     new_offset = None
    #today = now.day
    #hour = now.hour
     while True:
         greet_bot.get_updates(new_offset)
         last_update = greet_bot.get_last_update()
         last_update_id = last_update['update_id']
         #   last_chat_text = last_update['message']['text']
         last_chat_id = last_update['message']['chat']['id']
          #   last_chat_name = last_update['message']['chat']['first_name']
         greet_bot.send_message(last_chat_id, 'В дальнейшем сообщения о 0 непрочитанных сообщениях приходить не будут.') 
         greet_bot.send_message(last_chat_id, 'Это тестовая версия, на период отладки в целях изучения поведения бота.')
         
         s = requests.Session()
         r = s.post('https://portal4.cbr.ru/Account/Login', data = {'UserName':'leg10261021035762124', 'Password':'Hklm2070%'})
         r = s.get('https://portal4.cbr.ru//Notification/GetNotificationCount')
         greet_bot.send_message(last_chat_id, "У вас в личном кабинете есть непрочитанные сообщения в количестве " + r.text)
          
         #today += 1
         new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
