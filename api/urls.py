from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'surveyors', views.SurveyorViewSet)
router.register(r'survey', views.SurveyViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'available_options', views.Available_OptionsViewSet)
router.register(r'survey_info', views.Survey_InfoViewSet)
router.register(r'survey_answer', views.Survey_AnswerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]