import telebot
import config
import dbhandler
from textparser import check_entry, parse_entry

bot = telebot.TeleBot(config.KEY)

def calculate_gpa(subject_list):
    grade_list = [x[1] for x in subject_list] # no need for subject names

    total_gpa = 0 # a counter
    for grade in grade_list:
        total_gpa += config.GRADES[grade]

    return total_gpa / len(grade_list) # average GPA


@bot.message_handler(commands=['start']) # IDEA: FORCE REPLY??
def send_start(message):
    bot.send_message(message.chat.id, config.ENTER_REPLY, parse_mode='HTML')

@bot.message_handler(func=lambda m: '-' in m.text, content_types=['text'])
def record_results(message):
    if not check_entry(message.text):
        bot.send_message(message.chat.id, config.FORMAT_REPLY)
        return # no need to add the message to db as it is incorrect

    subject_list = parse_entry(message.text)
    subject, grade = subject_list # unpack the list to insert into function
    dbhandler.create_table(message)
    dbhandler.write_table(subject, grade, message)


@bot.message_handler(commands=['done'])
def send_results(message):
    data = dbhandler.pull_data(message)

    if not data:
        bot.send_message(message.chat.id, config.EMPTY_REPLY)
        return
        
    average_GPA = str(round(calculate_gpa(data), 2)) # GPA is 2 d.p.

    bot.send_message(message.chat.id, config.GPA_REPLY.format(average_GPA))

    dbhandler.delete_table(message) # so user can enter new classes next time

bot.polling()
