from instagrapi import Client
import schedule
import time

USERNAME = "daily.singh.greeting"
PASSWORD = "Param@2007"
VIDEO_PATH = "dailysinghgreeting.mp4"
CAPTION = "💸 Another reminder. Stay focused. #cashflow"

def post_video():
    try:
        cl = Client()
        cl.login(USERNAME, PASSWORD)
        cl.video_upload(VIDEO_PATH, CAPTION)
        print("Video Posted Successfully!")
    except Exception as e:
        print("Error Occurred:", e)

schedule.every().day.at("14:15").do(post_video)

print("Waiting to post daily...")

while True:
    print("Checking schedule...")
    schedule.run_pending()
    time.sleep(60)