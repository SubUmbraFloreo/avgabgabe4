import time
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import requests
import uuid
import json

# configuration for the Client
default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}

def kundendaten_erfassen(task: ExternalTask) -> TaskResult:

    neukunde = task.get_variable("neukunde")

    if neukunde == True :
        kundendaten_anfrage = "Bitte Kundenformular ausfüllen!"

    return task.complete()

ExternalTaskWorker(worker_id=2).subscribe("kundendatenErfassen", kundendaten_erfassen)
ExternalTaskWorker(worker_id=2).subscribe("kundendatenSpeichern", kundendaten_erfassen)