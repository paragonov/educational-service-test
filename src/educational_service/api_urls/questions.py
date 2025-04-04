from django.urls import path

from educational_service.questions.views import ThemeList, TestCaseResultsView, TestCaseResultsStatisticView

urlpatterns = [
    path('themes/', ThemeList.as_view(), name='themes'),
    path('results/', TestCaseResultsView.as_view(), name='results'),
    path('statistics/', TestCaseResultsStatisticView.as_view(), name='statistics'),
]