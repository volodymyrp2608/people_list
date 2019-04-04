from .views import DataPeopleRudView, DataPeopleAPIView
from django.urls import path

app_name = 'api-people'

urlpatterns = [
    path('', DataPeopleAPIView.as_view(), name='person-create'),
    path('<int:pk>/', DataPeopleRudView.as_view(), name='people-rud'),
]
