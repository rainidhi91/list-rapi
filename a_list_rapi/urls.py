from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
     
     path('country/', CountryListCreateAPIView.as_view(),name="country_list_create_view"),
     path('country/<uuid:country>/edit/',CountryRetrieveUpdateDestroyAPIView.as_view(), name="country_detail"),

     path('timezone/', TimezoneListCreateAPIView.as_view(),name="timezone_list_create_view"),
     path('timezone/<uuid:timezone>/edit/',TimezoneRetrieveUpdateDestroyAPIView.as_view(), name="timezone_detail"),

     path('city/', CityListCreateAPIView.as_view(), name="city_list_create_view"),
     path('city/<uuid:city>/edit/',CityRetrieveUpdateDestroyAPIView.as_view(), name="city_detail"),

     path('<uuid:city>/country/', CityCountryListAPIView.as_view(),name="city_country_list_view"),

     path('postcode/', PostcodeListCreateAPIView.as_view(),name="postcode_list_create_view"),
     path('postcode/<uuid:postcode>/edit/',PostcodeRetrieveUpdateDestroyAPIView.as_view(), name="postcode_detail"),

     path('<uuid:postcode>/city/', PostcodeCityListAPIView.as_view(),name="postcode_city_list_view"),

     path('<uuid:postcode>/postcode_country/', PostcodeCountryListAPIView.as_view(),name="postcode_country_list_view"),

     path('language/', LanguageListCreateAPIView.as_view(),name="language_list_create_view"),
     path('language/<uuid:language>/edit/',LanguageRetrieveUpdateDestroyAPIView.as_view(), name="language_detail"),

     path('country_language/', Country_LanguageListCreateAPIView.as_view(),name="country_language_list_create_view"),
     path('country_language/<uuid:country_language>/edit/',Country_LanguageRetrieveUpdateDestroyAPIView.as_view(), name="country_language_detail"),

     path('<uuid:country_language>/language_country/', Country_LanguageCountryListAPIView.as_view(),name="country_language_country_list_view"),
     path('<uuid:country_language>/language/', Country_LanguageLanguageListAPIView.as_view(),name="country_language_language_list_view"),

     path('social_media/', Social_MediaListCreateAPIView.as_view(),
          name="social_media_list_create_view"),
     path('social_media/<uuid:social_media>/edit/',
          Social_MediaRetrieveUpdateDestroyAPIView.as_view(), name="social_media_detail"),

     path('sic_code/', SIC_CodeListCreateAPIView.as_view(),
          name="sic_code_list_create_view"),
     path('sic_code/<uuid:sic_code>/edit/',
          SIC_CodeRetrieveUpdateDestroyAPIView.as_view(), name="sic_code_detail"),

     path('currency/', CurrencyListCreateAPIView.as_view(),name="currency_list_create_view"),
     path('currency/<uuid:currency>/edit/',CurrencyRetrieveUpdateDestroyAPIView.as_view(), name="currency_detail"),

     path('countrycurrency/', CountryCurrencyListCreateAPIView.as_view(),name="countrycurrency_list_create_view"),
     path('countrycurrency/<uuid:countrycurrency>/edit/',CountryCurrencyRetrieveUpdateDestroyAPIView.as_view(), name="countrycurrency_detail"),

     
]

