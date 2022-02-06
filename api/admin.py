import imp
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Surveyor)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Available_Options)
admin.site.register(Survey_Info)
admin.site.register(Survey_Answer)