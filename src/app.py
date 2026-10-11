import telebot
import base

# import app_api

bot = telebot.TeleBot(base.TOKEN)

print("Bot created ...")

@bot.message_handler(commands=["start"])
def send_message(message):
    bot.send_message(message.chat.id, text="به ربات آموزشی خوش آمدید")

@bot.message_handler(commands=["help", "support"])
def reply_message(message):
    bot.reply_to(message, text="در صورت نیاز به پشتیبانی با شماره 1505 تماس بگرید")

@bot.message_handler(commands=["news"])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text="اخبار ورزشی", url="https://varzesh3.com")
    btn2 = telebot.types.InlineKeyboardButton(text="اخبار عمومی", url="https://entekhab.ir")
    btn3 = telebot.types.InlineKeyboardButton(text="آپارات اسپورت", url="https://aparatsport.ir")
    
    markup.add(btn1, btn2 , btn3)
    bot.send_message(message.chat.id, text="یکی از گزینه های زیر را انتخاب کنید", reply_markup=markup)

@bot.message_handler(commands=["menu"])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton(text="درباره ما")
    btn2 = telebot.types.KeyboardButton(text="تماس با ما")
    btn3 = telebot.types.KeyboardButton(text="بازگشت")
    markup.add(btn1, btn2 , btn3)
    bot.send_message(message.chat.id,text="یکی از گزینه های زیر را انتخاب کنید", reply_markup=markup)

@bot.message_handler(func=lambda message:True)
def answer_to_other_msg(message):
    if message.text == "درباره ما":
        description = "بهترین بات"
        bot.send_message(message.chat.id, text=description)

    elif message.text == "تماس با ما":
        email = "support@ymail.com"
        mobile = "09166567240"
        office_add = "Tehran"
        info = f"راه های ارتباط: email: {email} - {mobile} - {office_add}"
        bot.reply_to(message, text=info)
    elif message.text == "بازگشت":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text="بازشگت به منوی اصلی" , reply_markup= markup)

    else:
        bot.send_message(message.chat.id, text="متوجه منظور شما نشدم")


if __name__ == "__main__":
    bot.infinity_polling()