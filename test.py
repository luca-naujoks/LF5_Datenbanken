"""import bcrypt

db_password = b'$2b$12$dm600OsnPaFH6kdTq8gSeuiVFXvMevFkOuouJNjRqMDgOjym1f1XC'
db_salt = b'$2b$12$dm600OsnPaFH6kdTq8gSeu'


user_password = "08Kasper06!"

user_password = user_password.encode("utf-8")

hashed = bcrypt.hashpw(user_password, db_salt)


if hashed == db_password:
    print("yes")
else:
    print("no")"""




import asyncio
import time

import PySimpleGUI as sg
import bcrypt
import re



import mysql.connector

mydb = mysql.connector.connect(
  host="server",
  user="bobby",
  password="08Kasper06!By",
  database="krautundrueben",
  port="3306"
)


login = ""
name = ""
geb = ""
ort = ""
street = ""
tele = ""
email = "fuck"



sg.theme('System Default1')


sg.popup("Herzlich wilkommen auf dem User Interface von Kraut & Rüben", no_titlebar=True)


main = [
        [sg.Text("                                                                                                                               "), sg.Button('Login')],
        [sg.Text('Search for recepies'), sg.InputText(key='_IN_')],
        [sg.Text(size=(40, 1), key='-OUTPUT-')],
        [sg.Button('Search')],
        [sg.Text("")],
        [sg.Button(' Exit ')]
        ]

layout2 = [[sg.Text("")],
           [sg.Text("E Mail Adresse"), sg.InputText(key='_Email_', size=40)],
           [sg.Text("Passwort        "), sg.InputText(key='_Passwd_', size=40)],
           [sg.Text("")],
           [sg.Button('Sign In'), sg.Text("        "), sg.Button('Back')]]

afterlogin = [
        [sg.Button('My Account'), sg.Text("                                                                                                                               "), sg.Button('Logout')],
        [sg.Text('Search for recepies'), sg.InputText(key='_IN_')],
        [sg.Text(size=(40, 1), key='-OUTPUT-')],
        [sg.Button('Search')],
        [sg.Text("")],
        [sg.Button(' Exit ')]
        ]
account = [
        [sg.Text(f"Name:                {name}")],
        [sg.Text(f"Birthday:            {geb}")],
        [sg.Text(f"Street:              {street}")],
        [sg.Text(f"Ort:                 {ort}")],
        [sg.Text(f"Telephone Number:    {tele}")],
        [sg.Text(f"E-Mail-Adress:       {email}")],
]



layout = [[sg.Column(main, key='-COL1-', visible=True), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(afterlogin, key='-COL3-', visible=False), sg.Column(account, key='-COL4-', visible=False)]]


window = sg.Window('K & R Grafical User Interface', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == ' Exit ':
        break

    if event == 'Search':
        mycursor = mydb.cursor()
        sql = f"SELECT REZEPTE.Rezeptname AS 'Rezepte', ZUTAT.BEZEICHNUNG AS 'Zutat' FROM REZEPTE INNER JOIN RELATIONTABLE ON REZEPTE.RezNR = RELATIONTABLE.RezNr INNER JOIN ZUTAT ON RELATIONTABLE.ZUTATENNR = ZUTAT.ZUTATENNR WHERE REZEPTE.Rezeptname = '{values['_IN_']}' ORDER BY ZUTAT.BEZEICHNUNG, REZEPTE.Rezeptname"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    if event == 'Search':
        mycursor = mydb.cursor()
        sql_1 = f"SELECT REZEPTE.Rezeptname AS 'Rezepte', ZUTAT.BEZEICHNUNG AS 'Enthält die Zutat' FROM REZEPTE INNER JOIN RELATIONTABLE ON REZEPTE.RezNR = RELATIONTABLE.RezNr INNER JOIN ZUTAT ON RELATIONTABLE.ZUTATENNR = ZUTAT.ZUTATENNR WHERE ZUTAT.BEZEICHNUNG = '{values['_IN_']}' ORDER BY REZEPTE.Rezeptname,ZUTAT.BEZEICHNUNG"
        mycursor.execute(sql_1)
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    if event == 'Search':
        mycursor = mydb.cursor()
        sql_art = f"SELECT REZEPTE.Rezeptname AS Rezepte From REZEPTE Where REZEPTE.Ernährungs_art = '{values['_IN_']}';"
        mycursor.execute(sql_art)
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    if event == 'Login':
        window['-COL1-'].update(visible=False)
        window['-COL2-'].update(visible=True)

    if event == 'Back':
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=True)



    #Der Fehler liegt an den ausgelesenen daten der DB (Eventuell falsches vormat)
    if event == 'Sign In':
        mycursor = mydb.cursor()
        sql_pswd = f"SELECT KUNDE.Passwd From KUNDE Where KUNDE.EMAIL = '{values['_Email_']}'"
        mycursor.execute(sql_pswd)
        db_password = mycursor.fetchone()[0]
        print("db_password: " + db_password)
        sql_salt = f"SELECT KUNDE.SALT From KUNDE Where KUNDE.EMAIL = '{values['_Email_']}'"
        mycursor.execute(sql_salt)
        db_salt = b'$2b$12$dm600OsnPaFH6kdTq8gSeu'


        user_password = values['_Passwd_'].encode()
        print(values['_Passwd_'])



        hashed = bcrypt.hashpw(
            user_password,
            db_salt
        )
        print(hashed)

        if hashed == db_password:
            print("login ok")
            window['-COL2-'].update(visible=False)
            window['-COL3-'].update(visible=True)
        else:
            print("fail")

    if event == 'My Account':
        email.append("hallo")
        window['-COL3-'].update(visible=False)
        window['-COL4-'].update(visible=True)
        mycursor = mydb.cursor()








#_Email_        _Passwd_
window.close()
