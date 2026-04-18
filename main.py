import telebot
import time

# آپ کا ٹوکن
TOKEN = '8654369776:AAGa0FvxyKG65E8AiQCEpZc57Iiy0ulFCKk'

# آپ کے پبلک چینل کا یوزرنیم (ایسا ہی ہونا چاہیے)
CHAT_ID = '@FS_Panther_Official'

bot = telebot.TeleBot(TOKEN)

def send_signal(message):
    try:
        bot.send_message(CHAT_ID, message, parse_mode="Markdown")
        print("Signal sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# بوٹ سٹارٹ کا میسج
print("FS Panther Bot is now Active!")
try:
    bot.send_message(CHAT_ID, "🚀 *FS Panther Bot is Online & Running 24/7!*")
except:
    print("Could not send startup message. Is the bot Admin in the channel?")

# مین لوپ
while True:
    # یہاں آپ اپنی ٹریڈنگ سگنل لاجک شامل کر سکتے ہیں
    time.sleep(60)
  
