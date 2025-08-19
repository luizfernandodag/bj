from app.workers.celery_app import celery

@celery.task(name="app.workers.tasks_ingest.ping")
def ping():
    return "pong"