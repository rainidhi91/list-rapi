from django.db import models
import uuid

class Currency(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=5, null=True, blank=True)
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Currencies"


class Country(models.Model):
    ''' list of countries in the world  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    iso2 = models.CharField(max_length=2, null=True, blank=True)
    iso3 = models.CharField(max_length=3, null=True, blank=True)
    dialcode = models.CharField(max_length=5, null=True, blank=True)
    # Africa, Europe, Asia, Antarctica, North America, South America, Oceania
    continent = models.CharField(max_length=100, null=True, blank=True)
    tld = models.CharField(max_length=5, null=True, blank=True)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"

class CountryCurrency(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT)
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.country.name} | {self.currency.name}"

    class Meta:
        verbose_name = "Country Currencies"


class Timezone(models.Model):
    ''' world's timezones and offsets from utc/gmt  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    code = models.CharField(max_length=5, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    utc_offset = models.SmallIntegerField(null=True, blank=True)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    ''' cities of the world  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    country =  models.ForeignKey(Country, on_delete=models.PROTECT)
    capital = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Cities"


class Postcode(models.Model):
    ''' world postodoes - starting with uk postcodes only  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    code = models.CharField(max_length=50,null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    region = models.CharField(max_length=50, null=True, blank=True)
    uk_region = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    longitude = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.code}"


class Language(models.Model):
    ''' world languages  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    iso_639_2 = models.CharField(max_length=3, null=True, blank=True)
    iso_639_1 = models.CharField(max_length=2, null=True, blank=True)
    english = models.CharField(max_length=50, null=True, blank=True)
    french = models.CharField(max_length=50, null=True, blank=True)
    german = models.CharField(max_length=50, null=True, blank=True)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.iso_639_2}"


class Country_Language(models.Model):
    ''' languages spoken in a particular country  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.country.name} | {self.language.name}"

    class Meta:
        verbose_name = "Country Language"


class Social_Media(models.Model):
    ''' list of social media platforms  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Social Media"


class SIC_Code(models.Model):
    '''UK standard industrial classification (SIC) codes that describe the business of a company  '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    code = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    # id of the user who is logged in and creating this record
    created_by = models.UUIDField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.code}"

    class Meta:
        verbose_name = "SIC Code"