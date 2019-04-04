from django.db import models

from rest_framework.reverse import reverse as api_reverse

class List_People(models.Model):
    """ Model list of people """
    user = models.ForeignKey('auth.User', db_column='Author', verbose_name='Author', null=False, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50, db_column='Surname', verbose_name='Surname')
    name = models.CharField(max_length=50, db_column='Name', verbose_name='Name')
    birthday = models.DateField(db_column='Birthday')
    mobile_phone = models.CharField(max_length=20,db_column='Mobile phone')

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    @property
    def owner(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse("api-people:people-rud", kwargs={'pk':self.pk}, request=request)
