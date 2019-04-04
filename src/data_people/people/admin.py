from django.contrib import admin
from .models import List_People


class ListPeopleAdmin(admin.ModelAdmin):
    """  List of people in the table """

    list_display = ('surname', 'name', 'birthday', 'mobile_phone')

    class Meta:
        model = List_People

admin.site.register(List_People, ListPeopleAdmin)
