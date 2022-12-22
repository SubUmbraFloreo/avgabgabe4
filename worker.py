from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import requests

# configuration for the Client
default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}


def daten_vergleichen(task: ExternalTask) -> TaskResult:

    print('Event angekommen')

    vorname = task.get_variable("prename")
    nachname = task.get_variable("surname")

    daten = requests.get('http://localhost:3000/customers')

    if daten.status_code > 300:
        print('Error')
        return task.failure()

    for person in daten.json():
        if vorname == person['prename'] and nachname == person['surname']:
            print('Name ist enthalten')
            return task.complete({'neukunde':'false'})

    return task.complete({'neukunde':'true'})


ExternalTaskWorker(worker_id=1).subscribe("neukunde", daten_vergleichen)