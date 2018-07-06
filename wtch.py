 #cbr_watchdog бот для автоматического уведомления о сообщениях в ЛК ЦБ РФ
import requests
s = requests.Session()
r = s.post('https://portal4.cbr.ru/Account/Login', data = {'UserName':'leg10261021035762124', 'Password':'Hklm2070%'})
r = s.get('https://portal4.cbr.ru//Notification/GetNotificationCount')
print("У вас в личном кабинете " + r.text + " непрочитанных сообщений")

