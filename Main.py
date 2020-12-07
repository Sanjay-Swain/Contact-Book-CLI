# v1.1
from Modules.MainModules import *
import os

os.makedirs('Contacts', exist_ok=True)
conn = sqlite3.connect('Contacts/contacts.db')

c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS contact_info (Name char(25), Phone char(25), Email char(40))')

print("Welcome")
print("Type help to know the commands")
# This part is broken for now after back-end update!
while True:
    Command = input(" --> ").lower().strip()
    if Command in command_list.keys():
        command_list[Command](c)
    elif Command == 'save' or Command == 'exit':
        break
    else:
        print('Command not found try again.')

conn.commit()
conn.close()
