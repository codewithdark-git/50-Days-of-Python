from plyer import notification
import time

if __name__ == "__main__":
    notification.notify(
        title="Remainder",
        message="This is A Remainder Code for display task ",
        timeout="10",
    )
    time.sleep(5)