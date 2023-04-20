from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
app = Celery("main")

#we are using asia/kolkata time so we are making it False
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Baku')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


app.conf.beat_schedule={
    'fetch_user_data':{
        'task':'account.tasks.check_instagram_profile',
        'schedule': 60,
        # 'args': (1,2)?
        # we can pass arguments here and we can use those in
        # firemailapp/tasks.py send_mail_func function for 
        # that you need one extra argument in your function
        # currently we are not doing that
        # 'args': (1000,)  
    }
}