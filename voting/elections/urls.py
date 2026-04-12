from django.urls import path
from .views import election_list, candidate_list, vote, results

urlpatterns = [
    path('', election_list, name='election_list'),
    path('<int:election_id>/', candidate_list, name='candidate_list'),
    path('vote/<int:candidate_id>/', vote, name='vote'),
    path('results/<int:election_id>/', results, name='results'),
]