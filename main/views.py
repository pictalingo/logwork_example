from rest_framework import generics
from rest_framework.response import Response

from main.models import Worker, Project
from main.serializers import WorkerSerializer, ProjectSerializer


from main.handlers import get_log, start_log_work, end_log_work


class WorkersView(generics.ListAPIView):
    model = Worker
    queryset = model.objects.all()
    serializer_class = WorkerSerializer

    def get_queryset(self, **kwargs):
        queryset = self.queryset.filter(**kwargs)
        return queryset


class ProjectsView(generics.ListAPIView):
    model = Project
    queryset = model.objects.all()
    serializer_class = ProjectSerializer


class CreateNewLogView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        worker_id = kwargs.get('worker_id', None)
        project_id = kwargs.get('project_id', None)
        if worker_id and project_id:
            try:
                worker = Worker.objects.get(pk=worker_id)
                project = Project.objects.get(pk=project_id)
            except:
                return Response({"ERROR": "Can't find user or project"})

            return Response(start_log_work(worker, project))


class EndLogView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        worker_id = kwargs.get('worker_id', None)
        project_id = kwargs.get('project_id', None)

        if worker_id and project_id:
            try:
                worker = Worker.objects.get(pk=worker_id)
                project = Project.objects.get(pk=project_id)
            except:
                return Response({"ERROR": "Can't find user or project"})

            return Response(end_log_work(worker, project))


class WorkLogView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        return Response(get_log())

