import imp
from django.contrib import admin
from .models import *
# Register your models here.

class SurveyorAdmin(admin.ModelAdmin):
    pass
class SurveyAdmin(admin.ModelAdmin):
    pass
class QuestionAdmin(admin.ModelAdmin):
    pass
class Available_OptionsAdmin(admin.ModelAdmin):
    pass
class Survey_InfoAdmin(admin.ModelAdmin):
    pass
class Survey_AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Surveyor, SurveyorAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Available_Options, Available_OptionsAdmin)
admin.site.register(Survey_Info, Survey_InfoAdmin)
admin.site.register(Survey_Answer, Survey_AnswerAdmin)