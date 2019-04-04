from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.data_people, name='list_people'),
    path('person/', views.person_create, name='person_create'),
    path('person/<int:pk>/update/', views.person_update, name='person_update'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('api/people', include('people.api.urls')),
    path('updated_list/', views.updated_list, name='updated_list')
    # path('api/v1/people/<int:pk>/', views.PersonDetail.as_view(), name='post-rud'),
    # path('person/create/', views.person_create, name='person_create'),
    # path('person/<int:pk>/update/', views.person_update, name='person_update'),
    # path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
]