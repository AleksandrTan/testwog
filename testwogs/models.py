from django.db import models


class ManageLogserver(models.Manager):
    def save_new_record(self, server_status, url_request, test_status='successfully',
                        message='No message', api_status=0):
        new_record = Logserver(server_status=server_status, api_status=api_status,
                               message=message, url_request=url_request, test_status=test_status)
        new_record.save()
        return new_record


class Logserver(models.Model):
    url_request = models.CharField(max_length=200, default='')
    test_status = models.CharField(max_length=200, default='successfully')
    server_status = models.SmallIntegerField(default=0)
    api_status = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=1000, default='No message')
    time_create = models.TimeField(auto_now_add=True)
    objects = ManageLogserver()