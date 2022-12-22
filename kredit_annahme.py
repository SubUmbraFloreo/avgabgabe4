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

def kredit_annahme(task: ExternalTask) -> TaskResult:
    
    logging.info('Kreditannahme wurde akzeptiert')
    return task.complete()

ExternalTaskWorker(worker_id=2).subscribe("kreditAnnahme", kredit_annahme)