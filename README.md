# FastAPI-RabbitMQ-Celery-MongoDB

The application's architecture leverages FastAPI for creating robust APIs, RabbitMQ for message queuing, Celery for distributed task execution, and MongoDB for storing task results. 

## To run:

```sh
docker compose build
docker compose up
```

## To try:

http://localhost:8000/docs

Trigger the start of a text file processing task.

    POST /process

Check the progress of the task with the specified ID and fetch the results if the task is complete.

    POST /check_progress/{task_id}