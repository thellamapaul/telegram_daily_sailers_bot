import sys
import telebot
from datetime import datetime

#take input of bot api like 'python bot.pi num:str'
BOT_TOKEN = sys.argv[1]

#create bot
bot = telebot.TeleBot(BOT_TOKEN)

#the magic
def sailer():
    now = datetime.now()
    #get day 0 (Monday) through 6 (Sunday)
    day = now.weekday()
    if day == 0 :
        return "https://pbs.twimg.com/ext_tw_video_thumb/1602226927628128261/pu/img/NN6B4pq8tfDuRHzi?format=jpg&name=large"
    elif day == 1 :
        return "https://pbs.twimg.com/ext_tw_video_thumb/1693968597113278464/pu/img/GuWtfJ4y7tpKPEjC.jpg"
    elif day == 2 :
        return "https://pbs.twimg.com/ext_tw_video_thumb/1699395093609013248/pu/img/URCcW0IHo3rd2mKB.jpg"
    elif day == 3 :
        return "https://static.wikia.nocookie.net/flippo/images/f/f5/SailerThursday.png/revision/latest/thumbnail/width/360/height/360?cb=20200828091826"
    elif day == 4 :
        return "https://static.wikia.nocookie.net/flippo/images/7/7a/Friday_sailer_1.jpg/revision/latest?cb=20200816053728"
    elif day == 5 :
        return "https://static.wikia.nocookie.net/flippo/images/4/4b/20200826_144152.jpg/revision/latest?cb=20200826222608"
    elif day == 6 :
        return "https://pbs.twimg.com/ext_tw_video_thumb/1708318900172283904/pu/img/ekxI1XtlgGchWjRY?format=jpg&name=large"
    else :
        return "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8f38eb1c-14a1-4aaa-8bcd-74f5f8cb9824/d6visq0-2cf9b990-dba6-4cab-b64b-4c690c6e5b65.jpg/v1/fill/w_1024,h_768,q_75,strp/mr__krabs_s_eyes_burn__by_tomandjerry123456789_d6visq0-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzY4IiwicGF0aCI6IlwvZlwvOGYzOGViMWMtMTRhMS00YWFhLThiY2QtNzRmNWY4Y2I5ODI0XC9kNnZpc3EwLTJjZjliOTkwLWRiYTYtNGNhYi1iNjRiLTRjNjkwYzZlNWI2NS5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.GxSDFGSJmISynR0khUr_J8gCjWmDpHqJshJMT1CUKL4"

#respond ahoy
@bot.message_handler(commands=['ahoy'])
def send_time(message):
    bot.send_photo(message.chat.id, sailer())

#respond echo
#@bot.message_handler(func=lambda msg: True)
#def echo_all(message):
#    bot.reply_to(message, "not a thing")

bot.infinity_polling()