import telebot
import base

bot = telebot.TeleBot(base.TOKEN)
print("bot created ....")

video_url = "https://samplefile.com/samples/download/video/mp4/mp4_15s_sample_file_868KB.mp4/"
photo_url = "https://www.technolife.com/image/gallery-3-TLP-167809_b1d8329d-e554-47a5-a5f3-dc4e8cc35b7c.png"
audio_url = "https://samplelib.com/lib/preview/mp3/sample-3s.mp3"
document_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

@bot.message_handler(commands=["media"])
def show_media(message):
    markup = telebot.types.InlineKeyboardMarkup()

    btn1 = telebot.types.InlineKeyboardButton(text="تصویر لوکال",callback_data="local_photo")
    btn2 = telebot.types.InlineKeyboardButton(text="تصویر آنلاین",callback_data="online_photo")

    markup.add(btn1,btn2)

    btn3 = telebot.types.InlineKeyboardButton(text="ویدیو لوکال",callback_data="local_video")
    btn4 = telebot.types.InlineKeyboardButton(text="ویدیو آنلاین",callback_data="online_video")

    markup.add(btn3,btn4)

    btn5 = telebot.types.InlineKeyboardButton(text="موزیک لوکال",callback_data="local_audio")
    btn6 = telebot.types.InlineKeyboardButton(text="موزیک آنلاین",callback_data="online_audio")

    markup.add(btn5,btn6)

    btn7 = telebot.types.InlineKeyboardButton(text="فایل لوکال",callback_data="local_document")
    btn8 = telebot.types.InlineKeyboardButton(text="فایل آنلاین",callback_data="online_document")

    markup.add(btn7,btn8)


    bot.send_message(message.chat.id, text="یکی از گزینه ها رو انتخاب کنید", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    call_id = call.message.chat.id

    if call.data == 'online_photo':
        bot.send_photo(call_id,photo_url, caption="نمونه تصویر آنلاین")

    elif call.data == 'local_photo':
        with open("./media/images.png", "rb") as photo:
            bot.send_photo(call_id, photo, caption="نمونه تصویر لوکال")

    elif call.data == 'online_video':
            bot.send_video(call_id,video_url, caption="نمونه تصویر آنلاین")
    
    elif call.data == 'local_video':
        with open("./media/129403-744385395.mp4", "rb") as video:
            bot.send_video(call_id, video, caption="نمونه تصویر لوکال")

    elif call.data == 'online_audio':
            bot.send_audio(call_id,audio_url, caption="نمونه تصویر آنلاین")
    
    elif call.data == 'local_audio':
        with open("./media/Baaghe-Baroon-Zadeh_Siavash.mp3", "rb") as audio:
            bot.send_audio(call_id, audio, caption="نمونه تصویر لوکال")
            
    elif call.data == 'online_document':
            bot.send_document(call_id,document_url, caption="نمونه تصویر آنلاین")
    
    elif call.data == 'local_document':
        with open("./media/پایانترم گسسته.pdf", "rb") as document:
            bot.send_document(call_id, document, caption="نمونه تصویر لوکال")
        

if __name__ == "__main__":
    bot.infinity_polling()