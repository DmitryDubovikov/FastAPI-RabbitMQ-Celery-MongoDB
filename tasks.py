import time

from celery import Celery
from loguru import logger

app = Celery(
    "ROFL",
    broker="amqp://rabbitmq:5672",
    backend="mongodb://mongodb:27017/task_results",
)


# This is the task that celery tries to execute. bind=True specifies the task is
# bound and are required for task retires and accessing the task status


@app.task(bind=True)
def start_processing(self):
    # Let's simulate a long-running task here.
    logger.info("Reading a book :|")
    with open("assets/data.txt", "r") as file:
        result = file.read()
    time.sleep(20)
    logger.info("Done reading a book :)")
    return result
