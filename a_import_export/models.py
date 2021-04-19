from django.db import models


class ImportCSV(models.Model):
    csv_file_name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.csv_file_name} || {self.id} || {self.timestamp}"


class ImportLog(models.Model):
    csv = models.ForeignKey(ImportCSV, on_delete = models.CASCADE)
    error_headline = models.CharField(max_length=200, blank = True, null = True)
    completed = models.BooleanField(default = False)
    error = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.csv.id} || {self.timestamp}"
