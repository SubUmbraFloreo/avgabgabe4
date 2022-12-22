from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import logging

# configuration for the Client
default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}

def filial_ablehnung(task: ExternalTask) -> TaskResult:
    
    logging.info('Filialleiter hat den Kredit abgelehnt')
    return task.complete()

ExternalTaskWorker(worker_id=2).subscribe("filialAblehnung", filial_ablehnung)