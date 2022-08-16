# Телеграм Бот
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_comans import *

app = ApplicationBuilder().token("5500264058:AAHaCAsUZqMLCH36tiLxJif5OOyrvoNh01g").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("sum", sum))
print('server start')
app.run_polling()


# import matplotlib.pyplot as plt #построение графика
# import numpy as np

# # # Fixing random state for reproducibility №столбики
# # np.random.seed(19680801)

# list = [1, 2, 3, 2, 7] #построение кривой
# plt.plot(list)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()


# import emoji  #Смайлики
# print(emoji.emojize('Python is :thumbs_up:'))


# from progress.bar import Bar  Показывает процесс закгрузки
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)  # задержка в 1 сек
#     bar.next()
# bar.finish()


# from isOdd import isOdd

# print(isOdd(0))
# print(isOdd(4))
