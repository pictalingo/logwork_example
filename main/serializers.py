from rest_framework import serializers
from main.models import Worker, Project, WorkLog


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('id', 'name')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name')


class WorkLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkLog
        fields = ('id', 'start_datetime')
