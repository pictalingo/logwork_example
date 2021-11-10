from main.models import Worker, Project, WorkLog
from datetime import datetime


def start_log_work(worker, project):
    exist_work_logs = WorkLog.objects.filter(worker=worker, end_datetime=None)

    if len(exist_work_logs) != 0:
        return {"ERROR": "You can start new log work, because you are working on another project"}

    try:

        work_log = WorkLog.objects.create(worker=worker, project=project, end_datetime=None)
        work_log.start_datetime = datetime.now()
        work_log.save()

        return {"SUCCESS": "You started new log"}

    except:
        return {"ERROR": "Error to create new log - maybe some parameter is wrong"}


def end_log_work(worker, project):
    try:

        work_log = WorkLog.objects.get(worker=worker, project=project, end_datetime=None)
        work_log.end_datetime = datetime.now()
        work_log.save()

        return {"SUCCESS": "*** Successfully finished ***"}

    except:
        return {"ERROR": "Can't find project, maybe you finished before?"}


def get_log():
    logs = WorkLog.objects.all().exclude(end_datetime=None)

    resp = {}
    for log in logs:

        worker = Worker.objects.get(pk=log.worker_id)
        worker_logs = resp.get(worker.name, None)
        if worker_logs is None:
            resp.update({worker.name: {}})

        project = Project.objects.get(pk=log.worker_id)
        project_times = resp[worker.name].get(project.name, None)
        if project_times is None:
            resp[worker.name].update({project.name: 0})

        start_hours_diff = log.start_datetime.hour
        end_hours_diff = log.end_datetime.hour
        hour_diff = start_hours_diff - end_hours_diff

        resp[worker.name][project.name] = resp[worker.name][project.name] + hour_diff

    return resp
