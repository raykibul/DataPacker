from django.db import models

# Create your models here.
class Surveyor(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    zilla = models.CharField(max_length=20)
    upazilla = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
class Survey(models.Model):
    name = models.CharField(max_length=100)
class Question(models.Model):
    answer_type_choices = (
        ('direct_answer', 'Direct Answer'),
        ('mcq_text', 'MCQ Text'),
        ('mcq_image', 'MCQ with Image'),
        ('mcq_others', 'MCQ Others'),
        ('boolean', 'Boolean'),
    )
    question_text = models.CharField(max_length=500)
    answer_type = models.CharField(choices=answer_type_choices, max_length=20)
    serial = models.CharField(max_length=11)
    image = models.CharField(max_length=200)
    survey_id = models.ForeignKey(Survey, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
	    return self.answer_type
class Available_Options(models.Model):
    question_id = models.ForeignKey(Question, blank=True, null=True, on_delete=models.SET_NULL)
    value = models.CharField(max_length=500)
    post_question = models.BigIntegerField(default=-1)
class Survey_Info(models.Model):
    surveyor_id = models.ForeignKey(Surveyor, blank=True, null=True, on_delete=models.SET_NULL)
    surveyee_name = models.CharField(max_length=50)
    surveyee_phone = models.CharField(max_length=15)
    surveyee_address = models.CharField(max_length=100)
    survey_id = models.ForeignKey(Survey, blank=True, null=True, on_delete=models.SET_NULL)
class Survey_Answer(models.Model):
    question_id = models.ForeignKey(Question, blank=True, null=True, on_delete=models.SET_NULL)
    answer_value = models.CharField(max_length=500)
    survey_info_id = models.ForeignKey(Survey_Info, blank=True, null=True, on_delete=models.SET_NULL)