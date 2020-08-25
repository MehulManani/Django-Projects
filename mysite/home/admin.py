from django.contrib import admin

from .models import Topic, WebPage, AccessRecords, Users

# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecords)
admin.site.register(Users)
