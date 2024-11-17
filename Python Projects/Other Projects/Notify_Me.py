import time
from plyer import notification

notification.notify(
    title = "Please Drink Water",
    message = "Water is very essential for our Body",
    app_icon = None,
    timeout = 3
    )

time.sleep(60 * 60)

