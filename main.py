import os
from flask import Flask
from threading import Thread

# បង្កើត Web Server តូចមួយសម្រាប់បំពេញលក្ខខណ្ឌ Render Web Service
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# កូដ Telegram Bot របស់អ្នកនៅទីនេះ...
if __name__ == "__main__":
    keep_alive()
    # កូដសម្រាប់รัน Bot ធម្មតារបស់คุณ (ឧទាហរណ៍: application.run_polling())