from django import forms


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise forms.ValidationError("Only CSV file is accepted")


class CSVFileUploadForm(forms.Form):
    file = forms.FileField(label = "Select a CSV File To Import", validators = [validate_file_extension,])