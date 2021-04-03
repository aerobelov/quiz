from django.urls import path

from .views import SetsView, QuestionView, UserAnswersView, SaveUserAnswerView
#app_name = "quiz_api"

urlpatterns = [
    path('sets/', SetsView.as_view()),
    path('question/<int:index>', QuestionView.as_view()),
    path('user_answer/<int:user_id>', UserAnswersView.as_view()),
    path('save/', SaveUserAnswerView.as_view()),
]