global kud
global otk
global usi 


kud=0
otk=0
usid=0
import telebot
#import configparser
import json
import requests
import mysql.connector
from mysql.connector import Error
import baza16.py

conn = mysql.connector.connect(
         user='root',
         password='lizard',
         host='localhost',
         database='tele')






Token1="948381879:AAEO07_DU1z-CO67NRWIi8HX_jeLNfQVqPo"
bot = telebot.TeleBot(Token1)
@bot.message_handler(commands=['start'])
def start_command(message):
    global otk
    global usi
    user_id = message.from_user.id
    #работа с ьазой
    print('user_id=',user_id)
    bot.send_message( message.chat.id, "выберите чат для пересылки")
    print('message.chat.id1=',message.chat.id)
    otk=message.chat.id
    print('otk= ',otk)
    usi=user_id
@bot.message_handler(commands=['help'])
def start_command(message):
  global kud
  bot.send_message( message.chat.id,  "Хорошо")
  print('message.chat.id=', message.chat.id)
  kud=message.chat.id
  print('kud=',kud)
  
@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
   global otk
   indikator=0
   print ('kudprom=',kud)
   if (message.chat.id!=kud):print( message.chat.id)
   else: print ('kudprom=',kud)
   if (message.chat.id!=kud):       
       if message.text[0]=="#":                          
            bot.forward_message(kud ,otk, message.message_id)
            print('newkud=',kud)
            print('newotk=', otk)
            indikator=1
            #запись в базу
            print('kud=',kud)
            print('otk=', otk)
            print('usi=',usi)
            baza(kud,otk,usi,text)




            
   else :
       print("пишите в чат где старт")
       bot.send_message( kud,  "пишите в чат где start")



bot.polling()

