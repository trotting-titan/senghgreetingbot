from instagrapi import Client
import schedule
import time
import sys
import os

# 👇 Makes paths work even inside .exe
def resource_path(filename):
    try:
        base_path = sys._MEIPASS  # Used when running as .exe
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)

# File paths (adjusted for .exe)
USERNAME = "daily.singh.greeting"
PASSWORD = "Param@2007"
SESSION_FILE = resource_path("session.json")
VIDEO_PATH = resource_path("dailysinghgreeting.mp4")
DAY_COUNTER_FILE = resource_path("day_counter.txt")

def get_next_caption():
    # If file doesn't exist, start at Day 1
    if not os.path.exists(DAY_COUNTER_FILE):
        with open(DAY_COUNTER_FILE, "w") as f:
            f.write("1")

    with open(DAY_COUNTER_FILE, "r") as f:
        day = int(f.read().strip())

    caption = f"Day {day} of Daily Singh Greeting"

    # Save next day
    with open(DAY_COUNTER_FILE, "w") as f:
        f.write(str(day + 1))

    return caption

def post_video():
    try:
        cl = Client()

        # Load or create session
        if os.path.exists(SESSION_FILE):
            cl.load_settings(SESSION_FILE)
            cl.login(USERNAME, PASSWORD)
        else:
            cl.login(USERNAME, PASSWORD)
            cl.dump_settings(SESSION_FILE)

        caption = get_next_caption()

        cl.video_upload(VIDEO_PATH, caption)
        print(f"✅ Video Posted: {caption}")

    except Exception as e:
        print("❌ Error Occurred:", e)

# ✅ Post immediately when run
post_video()

# ⏰ Schedule it to run daily at 14:04 (optional)
schedule.every().day.at("14:04").do(post_video)

print("⏳ Waiting for daily schedule...")

while True:
    schedule.run_pending()
    time.sleep(60)