import requests

TOKEN = "8336610986:AAHNix94slZShIlvQZxeRXQjpWFKEiKDbfA"
CHAT_ID = "@houshmandsho"

message = "⏰ پیام زمان‌بندی‌شده از ربات (تست موفق)!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": message
}

r = requests.post(url, data=data)
print("Status:", r.status_code)
print("Response:", r.text)
