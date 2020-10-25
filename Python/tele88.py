global kud
global otk


kud=0
otk=0
import telebot
#import configparser
import json
import requests
Token1="948381879:AAEO07_DU1z-CO67NRWIi8HX_jeLNfQVqPo"
bot = telebot.TeleBot(Token1)
@bot.message_handler(commands=['start'])
def start_command(message):
    global otk
    user_id = message.from_user.id
    print('user_id=',user_id)
    bot.send_message( message.chat.id, "выберите чат для пересылки")
    print('message.chat.id1=',message.chat.id)
    otk=message.chat.id
    print('otk= ',otk)
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
   else :
       print("пишите в чат где старт")
       bot.send_message( kud,  "пишите в чат где start")
bot.polling()

