from celery import shared_task

import time

@shared_task
def add_numbers(a, b):
    time.sleep(5)
    return a + b