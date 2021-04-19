from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework import fields
from .models import *
import requests
from django.utils.timesince import timesince


class CountrySerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(CountrySerializer, self).__init__(*args, **kwargs)


class TimezoneSerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = Timezone
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(TimezoneSerializer, self).__init__(*args, **kwargs)


class CitySerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(CitySerializer, self).__init__(*args, **kwargs)

        self.fields["country"].queryset = Country.objects.all()


class PostcodeSerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = Postcode
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(PostcodeSerializer, self).__init__(*args, **kwargs)

        self.fields["city"].queryset = City.objects.all()

        self.fields["country"].queryset = Country.objects.all()


class LanguageSerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = Language
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(LanguageSerializer, self).__init__(*args, **kwargs)


class Country_LanguageSerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = Country_Language
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(Country_LanguageSerializer, self).__init__(*args, **kwargs)

        self.fields["country"].queryset = Country.objects.all()
        self.fields["language"].queryset = Language.objects.all()


class Social_MediaSerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = Social_Media
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(Social_MediaSerializer, self).__init__(*args, **kwargs)


class SIC_CodeSerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = SIC_Code
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(SIC_CodeSerializer, self).__init__(*args, **kwargs)


class CurrencySerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(CurrencySerializer, self).__init__(*args, **kwargs)

class CountryCurrencySerializer(serializers.ModelSerializer):
    ''' description of class '''
    date_created = serializers.SerializerMethodField()

    class Meta:
        model = CountryCurrency
        fields = "__all__"
        # CHECK WHETHER MORE FIELDS NEED TO BE READ ONLY
        read_only_fields = ("id", "created_by", "date_created",)

    def get_date_created(self, instance):
        ''' function description '''
        return timesince(instance.date_created)

    def __init__(self, *args, **kwargs):

        super(CountryCurrencySerializer, self).__init__(*args, **kwargs)

        self.fields["country"].queryset = Country.objects.all()
        self.fields["currency"].queryset = Currency.objects.all()
