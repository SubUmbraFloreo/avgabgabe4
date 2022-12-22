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

def kundendaten_speichern(task: ExternalTask) -> TaskResult:
    
        prename = task.get_variable("prename")
        surname = task.get_variable("surname")
        creditRating = task.get_variable("creditRating")
        income = task.get_variable("income")
        bankLoans = task.get_variable("bankLoans")

        bla = {
            "id": str(uuid.uuid4()),
            "prename": prename,
            "surname": surname,
            "creditRating": creditRating,
            "income": income,
            "bankLoans": bankLoans
        }

        daten = requests.post('http://localhost:3000/customers', bla)

        if daten.statuscode > 300:
            print('Error')
            return task.failure()
        
        return task.complete()
    
ExternalTaskWorker(worker_id=2).subscribe("kundendatenSpeichern", kundendaten_speichern)