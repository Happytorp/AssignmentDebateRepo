from django.urls import path
from .views import debate_list, debate_challenge,debatelistforuser


urlpatterns = [
    path('list/', view=debate_list, name='dashboard'),
    path('list/<int:pk>', view=debate_challenge, name='challenge'),
    path('listuser/', view=debatelistforuser, name='userlist'),
]
