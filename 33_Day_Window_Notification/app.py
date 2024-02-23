import datetime
import schedule
import time
from plyer import notification

def send_notification(task_name):
    current_time = datetime.datetime.now().strftime("%d %H:%M")
    notification.notify(
        title="Task Reminder!!",
        message=f"{current_time}\n{task_name}",
        timeout=10,
        app_name="Your App Name",  # Change this to your app's name
        app_icon="D:\CodeBackground\pythonProject\WindowNotification\icon.ico",  # Add the path to your app's icon file
        ticker="Notification Ticker",  # Optional ticker text
        toast=True,  # Display as a Windows toast notification
        notification_id=123,  # Unique ID for the notification
        # Custom styling options
        app_color=(255, 0, 0),  # RGB color (red in this example)
        font=("Arial", 16),  # Font family and font size
    )

def convert_to_24_hour_format(time_str):
    try:
        time_24 = datetime.datetime.strptime(time_str, '%I:%M %p').strftime('%H:%M')
        return time_24
    except ValueError:
        return None

# Get user input for the task time and name in AM/PM format
enter_time = input("Enter the time to schedule the task (hh:mm AM/PM): ")
task_name = input("Enter Your Message: ")

# Convert the input time to 24-hour format
time_24_hour = convert_to_24_hour_format(enter_time)

if time_24_hour is not None:
    # Schedule the notification
    schedule.every().day.at(time_24_hour).do(send_notification, task_name)

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    print("Invalid time format. Please use hh:mm AM/PM format.")
