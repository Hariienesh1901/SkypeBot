import userpass
from skpy import Skype
import sys
import sys

sk = Skype(userpass.Hariiienesh1901["email"], userpass.Hariiienesh1901["password"])

User = input('Who do you want to send the message to: ')

if User == 'Kavienraj':
    contact = sk.contacts['live:2e681ff6ffaa0086']

    kind = input('What type do you want to send: ')


def message():
    if kind == 'msg':
        msg = input('What do you want to send: ')
        contact.chat.sendMsg(msg)
        print(contact.chat.getMsgs())

    elif kind == 'file':
        file = input('Where is your file located: ')
        name = input('What name do you want to send as: ')
        viewmsgs = contact.chat.sendFile(open(file, "rb"), name)
        print(viewmsgs)

while True:
    message()