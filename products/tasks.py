from project.celery import celery
import time


@celery.task
def send_m_email():
    for x in range(10):
        print(f'sending messege to {x}')
        time.sleep(10)