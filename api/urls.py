from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
#router.register(r'surveyors', views.SurveyorViewSet)
#router.register(r'survey', views.SurveyViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'available_options', views.Available_OptionsViewSet)
router.register(r'survey_info', views.Survey_InfoViewSet)
router.register(r'survey_answer', views.Survey_AnswerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('saveanswer/', views.saveAnswer, name='save answer'),
    path('surveyor/',views.SurveyorViewSet.as_view()),
    path('survey/',views.SurveyViewSet.as_view())
]
