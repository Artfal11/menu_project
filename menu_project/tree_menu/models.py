from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    menu_name = models.CharField(max_length=100, db_index=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        return self.url or '#'
