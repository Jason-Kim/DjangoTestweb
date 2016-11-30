# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 테이블 네임은 "application name_model class name" => search_report
class Report(models.Model):
    id_kipi = models.CharField(max_length=32, blank=False, primary_key=True)
    title = models.CharField(max_length=2048, blank=False)
    reference = models.CharField(max_length=512, blank=False)
    summary = models.CharField(max_length=1024*50, blank=False)     # use instead models.TextField
    
    def __str__(self):
        return self.id_kipi