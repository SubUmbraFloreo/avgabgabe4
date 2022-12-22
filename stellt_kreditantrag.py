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



def stellt_kreditantrag(task: ExternalTask) -> TaskResult:
    
    prename = task.get_variable("prename")
    surname = task.get_variable("surname")
    creditRating = task.get_variable("creditRating")
    income = task.get_variable("income")
    bankLoans = task.get_variable("bankLoans")

    logging.info(prename + ', ' + surname + ', ' + creditRating + ', ' + income + ', ' + bankLoans)
    
    return task.complete()
    

ExternalTaskWorker(worker_id=2).subscribe("stelltKreditantrag", stellt_kreditantrag)