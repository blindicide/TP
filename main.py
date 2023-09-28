import telebot
from telebot import types

tokenfile = open("token.txt", "r")
token = tokenfile.read()

bot = telebot.TeleBot(token)

