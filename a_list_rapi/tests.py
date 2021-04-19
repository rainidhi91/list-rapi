import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


# Create your tests here.
class ListTestCase(APITestCase):

    def setUp(self):
        self.Country= Country.objects.create(name="test",iso2="1",iso3="1",capital="test",dialcode="123",currency="test",continent="test",tld="1")
        
        

    def api_authentication(self):

        # Testcase for passing token for authorization

        self.client.credentials(HTTP_AUTHORIZATION = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MjI1NDc3LCJqdGkiOiIyYTUyODFmNTY4Yjk0NGJmYTA4ZWFmN2NkMDU3OTQwZiIsInVzZXJfaWQiOjd9.cW0p_QXRpjltjHoFUkivZmC4n0dZFi3AMn0oUfE1pZY")   

    
    def test_create_new_Country(self):

        #Testcase for creating Country

        self.api_authentication()
        response = self.client.post(reverse('country_list_create_view'),{
        "name": "test",
        "iso2": "1",
        "iso3": "1",
        "capital": "test",
        "dialcode": "123",
        "currency": "test",
        "continent": "test",
        "tld": "1"
        })
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = response.json()
        print("Country Created")

    def test_get_all_Country(self):

        #Testcase for getting Artifact

        self.api_authentication()
        response = self.client.get(reverse('country_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("Country Found")


    def test_create_new_Timezone(self):

        #Testcase for creating Country

        self.api_authentication()
        response = self.client.post(reverse('timezone_list_create_view'),{
         "code": "test",
        "name": "test"
        })
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = response.json()
        print("Timezone Created")

    def test_get_all_Timezone(self):

        #Testcase for getting Artifact

        self.api_authentication()
        response = self.client.get(reverse('timezone_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("Timezone Found")


    def test_create_new_Language(self):

        #Testcase for creating Country

        self.api_authentication()
        response = self.client.post(reverse('language_list_create_view'),{
        "iso_639_2": "tes",
        "iso_639_1": "te",
        "english": "test",
        "french": "test",
        "german": "test"
        })
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = response.json()
        print("Language Created")

    def test_get_all_Language(self):

        #Testcase for getting Artifact

        self.api_authentication()
        response = self.client.get(reverse('language_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("Language Found")


    def test_create_new_Social_Media(self):

        #Testcase for creating Country

        self.api_authentication()
        response = self.client.post(reverse('social_media_list_create_view'),{
        "url": "http://www.google.com"
        })
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = response.json()
        print("Social_Media Created")

    def test_get_all_Social_Media(self):

        #Testcase for getting Artifact

        self.api_authentication()
        response = self.client.get(reverse('social_media_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("Social_Media Found")

    def test_create_new_SIC_Code(self):

        #Testcase for creating SIC Code

        self.api_authentication()
        response = self.client.post(reverse('sic_code_list_create_view'),{
        "code": "test",
        "description": "test"
        })
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = response.json()
        print("SIC Code Created")

    def test_get_all_SIC_Code(self):

        #Testcase for getting Artifact

        self.api_authentication()
        response = self.client.get(reverse('sic_code_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("SIC Code Found")

    
    def test_get_all_Country_Language(self):

        #Testcase for getting Country_Language

        self.api_authentication()
        response = self.client.get(reverse('country_language_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("Country_Language Found")

    
    def test_get_all_Postcode(self):

        #Testcase for getting Postcode

        self.api_authentication()
        response = self.client.get(reverse('postcode_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("Postcode Found")


    def test_get_all_City(self):

        #Testcase for getting City

        self.api_authentication()
        response = self.client.get(reverse('city_list_create_view'))
    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("City Found")
