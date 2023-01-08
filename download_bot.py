import telebot
import urllib
import youtube_dl

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['download'])
def download(message):
    chat_id = message.chat.id
    text = message.text
    url_start_position = text.find('https://')
    url = text[url_start_position:]
    
    video_name = url.split('=')[1]
    ydl_opts = {
    'outtmpl': '/temp/' + video_name + '.mp4',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    doc = open('/temp/' + video_name + '.mp4', 'rb')
    bot.send_document(chat_id, doc)

bot.polling()