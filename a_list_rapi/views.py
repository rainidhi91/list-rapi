from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView, CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status, Response
from django.http import JsonResponse, HttpResponse


class CountryListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = CountrySerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return Country.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(CountryListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = CountrySerializer

    def get_object(self):
        return get_object_or_404(Country, created_by=self.request.user.id, id=self.kwargs.get("country"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(CountryRetrieveUpdateDestroyAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class TimezoneListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = TimezoneSerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return Timezone.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(TimezoneListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class TimezoneRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = TimezoneSerializer

    def get_object(self):
        return get_object_or_404(Timezone, created_by=self.request.user.id, id=self.kwargs.get("timezone"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(TimezoneRetrieveUpdateDestroyAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class CityListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = CitySerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return City.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(CityListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class CityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = CitySerializer

    def get_object(self):
        return get_object_or_404(City, created_by=self.request.user.id, id=self.kwargs.get("city"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(CityRetrieveUpdateDestroyAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class CityCountryListAPIView(ListAPIView):
    serializer_class = CountrySerializer

    def get_city_or_404(self):
        return get_object_or_404(City, created_by=self.request.user.id, pk=self.kwargs.get("city"))

    def get_queryset(self):
        return Country.objects.filter(created_by=self.request.user.id, city=self.get_city_or_404())

    def get_serializer_context(self):

        context = super(CityCountryListAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class PostcodeListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = PostcodeSerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return Postcode.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(PostcodeListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class PostcodeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = PostcodeSerializer

    def get_object(self):
        return get_object_or_404(Postcode, created_by=self.request.user.id, id=self.kwargs.get("postcode"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(PostcodeRetrieveUpdateDestroyAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class PostcodeCityListAPIView(ListAPIView):
    serializer_class = CitySerializer

    def get_postcode_or_404(self):
        return get_object_or_404(Postcode, created_by=self.request.user.id, pk=self.kwargs.get("postcode"))

    def get_queryset(self):
        return City.objects.filter(created_by=self.request.user.id, postcode=self.get_postcode_or_404())

    def get_serializer_context(self):

        context = super(PostcodeCityListAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class PostcodeCountryListAPIView(ListAPIView):
    serializer_class = CountrySerializer

    def get_postcode_or_404(self):
        return get_object_or_404(Postcode, created_by=self.request.user.id, pk=self.kwargs.get("postcode"))

    def get_queryset(self):
        return Country.objects.filter(created_by=self.request.user.id, postcode=self.get_postcode_or_404())

    def get_serializer_context(self):

        context = super(PostcodeCountryListAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class LanguageListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = LanguageSerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return Language.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(LanguageListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class LanguageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = LanguageSerializer

    def get_object(self):
        return get_object_or_404(Language, created_by=self.request.user.id, id=self.kwargs.get("language"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(LanguageRetrieveUpdateDestroyAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class Country_LanguageListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = Country_LanguageSerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return Country_Language.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(Country_LanguageListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class Country_LanguageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = Country_LanguageSerializer

    def get_object(self):
        return get_object_or_404(Country_Language, created_by=self.request.user.id, id=self.kwargs.get("country_language"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(Country_LanguageRetrieveUpdateDestroyAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context




class Country_LanguageCountryListAPIView(ListAPIView):
    serializer_class = CountrySerializer

    def get_country_language_or_404(self):
        return get_object_or_404(Country_Language, created_by=self.request.user.id, pk=self.kwargs.get("country_language"))

    def get_queryset(self):
        return Country.objects.filter(created_by=self.request.user.id, country_language=self.get_country_language_or_404())

    def get_serializer_context(self):

        context = super(Country_LanguageCountryListAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context



class Country_LanguageLanguageListAPIView(ListAPIView):
    serializer_class = LanguageSerializer

    def get_country_language_or_404(self):
        return get_object_or_404(Country_Language, created_by=self.request.user.id, pk=self.kwargs.get("country_language"))

    def get_queryset(self):
        return Language.objects.filter(created_by=self.request.user.id, country_language=self.get_country_language_or_404())

    def get_serializer_context(self):

        context = super(Country_LanguageLanguageListAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class Social_MediaListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = Social_MediaSerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return Social_Media.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(Social_MediaListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class Social_MediaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = Social_MediaSerializer

    def get_object(self):
        return get_object_or_404(Social_Media, created_by=self.request.user.id, id=self.kwargs.get("social_media"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(Social_MediaRetrieveUpdateDestroyAPIView,self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class SIC_CodeListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = SIC_CodeSerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return SIC_Code.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(SIC_CodeListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class SIC_CodeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = SIC_CodeSerializer

    def get_object(self):
        return get_object_or_404(SIC_Code, created_by=self.request.user.id, id=self.kwargs.get("sic_code"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(SIC_CodeRetrieveUpdateDestroyAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class CurrencyListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = CurrencySerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return Currency.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(CurrencyListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context


class CurrencyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = CurrencySerializer

    def get_object(self):
        return get_object_or_404(Currency, created_by=self.request.user.id, id=self.kwargs.get("currency"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(CurrencyRetrieveUpdateDestroyAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context



class CountryCurrencyListCreateAPIView(ListCreateAPIView):
    ''' class description '''
    serializer_class = CountryCurrencySerializer

    def perform_create(self, serializer):
        ''' function description '''
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        ''' function description '''
        return CountryCurrency.objects.filter(created_by=self.request.user.id)

    def get_serializer_context(self):
        ''' function description '''

        context = super(CountryCurrencyListCreateAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context

class CountryCurrencyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ''' class description '''

    serializer_class = CountryCurrencySerializer

    def get_object(self):
        return get_object_or_404(CountryCurrency, created_by=self.request.user.id, id=self.kwargs.get("countrycurrency"))

    def get_serializer_context(self):
        ''' function description '''

        context = super(CountryCurrencyRetrieveUpdateDestroyAPIView, self).get_serializer_context()

        context["created_by"] = self.request.user.id

        return context