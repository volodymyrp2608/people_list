from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from people.models import List_People

User = get_user_model()



class ListPeopleAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='Vova', email='vovapeleh1997@gmail.com')
        user_obj.set_password('1997wireless')
        user_obj.save()
        person = List_People.objects.create(
            user=user_obj,
            surname='Mon',
            name='Alex',
            birthday='1980-06-08',
            mobile_phone='+380687036523'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_person(self):
        person_count = List_People.objects.count()
        self.assertEqual(person_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse("api-people:person-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list(self):
        data = {"surname":"Messi", "name":"Leo", "birthday":"1986-08-06", "mobile_phone":"380989776456"}
        url = api_reverse("api-people:person-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        list_people = List_People.objects.first()
        data = {}
        url = list_people.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        person = List_People.objects.first()
        url = person.get_api_url()
        data = {"surname":"Messi", "name":"Leo", "birthday":"1986-08-06", "mobile_phone":"380989776456"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_user(self):
        person = List_People.objects.first()
        url = person.get_api_url()
        data = {"surname":"Messi", "name":"Leo", "birthday":"1986-08-06", "mobile_phone":"380989776456"}
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp) #JWT <token>
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_with_user(self):
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>
        data = {"surname":"Messi", "name":"Leo", "birthday":"1986-08-06", "mobile_phone":"380989776456"}
        url = api_reverse("api-people:person-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_ownership(self):
        owner = User.objects.create(username='test_volodymyr')
        person = List_People.objects.create(
            user=owner,
            surname='Mon',
            name='Alex',
            birthday='1980-06-08',
            mobile_phone='+380687036523'
        )
        user_obj = User.objects.first()
        self.assertNotEqual(user_obj.username, owner.username)
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>

        url = person.get_api_url()
        data = {"surname": "Messi", "name": "Leo", "birthday": "1986-08-06", "mobile_phone": "380989776456"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_login_and_update(self):
        data = {
            'username':'Vova',
            'password': '1997wireless'
        }
        url = api_reverse("api-login")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get("token")
        if token is not None:
            person = List_People.objects.first()
            url = person.get_api_url()
            data = {"surname": "Messi", "name": "Leo", "birthday": "1986-08-06", "mobile_phone": "380989776456"}
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)  # JWT <token>
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
