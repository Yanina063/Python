from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
from spy import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.now().time()}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg =  update.message.text
    print(msg)
    items = msg.split() #три элемента разделить пробелами (/sum, первое число и второе число)
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')