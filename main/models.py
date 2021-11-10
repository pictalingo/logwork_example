from django.db import models
from django.utils.translation import ugettext_lazy as _


class Worker(models.Model):
    name = models.CharField(_('Name'), max_length=254, db_index=True)


class Project(models.Model):
    name = models.CharField(_('Name'), max_length=1000, db_index=True)


class WorkLog(models.Model):
    worker = models.ForeignKey(Worker, verbose_name=_('Worker'), on_delete=models.PROTECT)
    project = models.ForeignKey(Project, verbose_name=_('Project'), on_delete=models.PROTECT)
    start_datetime = models.DateTimeField(_("Start work in"), blank=True, null=True, auto_now=False)
    end_datetime = models.DateTimeField(_("End work in"), blank=True, null=True, auto_now=False)
