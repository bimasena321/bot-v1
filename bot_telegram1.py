from api_key.apikey import apikey as key
from respon.respon import respon as R
import os as a
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ContextTypes, CallbackQueryHandler, ChosenInlineResultHandler, InlineQueryHandler
from telegram.ext import *


a.system('clear')
print("bot dinyalakan....")
def start(update, context):
    update.message.reply_text("Halo aku bot bima salam kenal")
def help(update, context):
    update.message.reply_text("""
                              /help
                              /start
                              /yt
                              /fb
                              /ig
                              /excel
                              /word/ppt
                              """)
def handle_pesan(update,context):
    text = str(update.message.text).lower()
    respon = R.respon_sample(text)
    update.message.reply_text(respon)
    
def error(update, context):
    print (f"update{update} error karena {context}")
    
    
def main():
    update = Updater(key.kunci_api, use_context=True)
    dd = update.dispatcher
    dd.add_handler(CommandHandler("start", start))
    dd.add_handler(CommandHandler("help", help))
    dd.add_handler(MessageHandler(Filters.text, handle_pesan))
    dd.add_error_handler(error)
    update.start_polling()
    update.idle()
    
main()
