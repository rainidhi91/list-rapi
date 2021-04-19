from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.apps import apps
from .forms import CSVFileUploadForm
import pandas as pd
from celery.decorators import task
import sqlite3
import csv
from datetime import datetime, timedelta
import string
import secrets
from .models import ImportCSV, ImportLog


def get_model(models, a_model):
    for model in models:

        if a_model == model.__name__:
            return model

    return None


def validate_columns(df, columns):

    for column in columns:

        if not f"{column.name}" in df.columns:
            return f"{column.name}"

    return True


#def aamir_hamza():

#     connection = sqlite3.connect(
#         "/Users/Aamir/Tech/GitLab/Lists/list-rapi/db.sqlite3")
#     connection.row_factory = sqlite3.Row

#     cursor = connection.cursor()


#     sql_text = f"""INSERT INTO {modelname}("{modelname}"""

#     for field in fields:
#         sql_text += f" {field name},"

#     sql_text += f") VALUES ("

#     for csv_col in csv_cols:
#         sql_text += f"?, "

#     sql_text += f")""" "

# #    values = f"(row["


#     commit_size = 1000

#     with open('/Users/Aamir/GoogleDrive/Investments/GIQ/04 PRODUCT/Microservices/Lists-DataFiles/city_remaining_0.csv') as f:
#         rows = csv.reader(f)
 
#         sql_insert = f" {sql_text}, "
#         jndx = 0

#         for row in rows:
#             jndx += 1
#             for indx 1 to len(row):
#                 values += f", {row(indx)}"

#             insert_values=f"{sql_text} + {values} )"
#             cursor.execute(insert_values)
#             if jndx % commit_size = 0 
#                 connection.commit()

#             #    """ INSERT INTO [MODELNAME]] ([FIELD1], [FIELD2], ...)
#             #     VALUES (?, ?, ETC ETC)
#             # """, (row['field1'], row['field1'], etc etc)

#     connection.close()


@task(name="import csv data to db")
def import_csv_data_to_db(import_id, colsdata, model):

    model=get_model(apps.get_models(), model)

    log = ImportLog.objects.create(csv_id = import_id)

    columns=model._meta.fields

    df_columns=list(map(lambda data: data[-1], colsdata.items()))

    for data in zip(*df_columns):
        import_data={}

        for index, column in enumerate(columns):

            if not column.get_internal_type() == "ForeignKey" and not column.get_internal_type() == "BooleanField":
                import_data[column.name]=data[index]

            elif column.get_internal_type() == "BooleanField":
                import_data[column.name]=bool(data[index])

            elif column.get_internal_type() == "ForeignKey":
                import_data[f"{column.name}_id"]=data[index]

        try:
            model.objects.create(**import_data)
        except Exception as e:
            log.error_headline = str(e)
            if not log.error:
                log.error = True
            log.save()
            break

    if not log.error:
        log.completed = True
        log.save()

@ staff_member_required
def import_view(request):

    models=apps.get_models()

    print(models)

    errors={}
    context={}

    if not request.GET.get("model") or not request.GET.get("model") in list(map(lambda model: model.__name__, models)):
        errors["model"]="Model Name isn't Correct!"

    else:

        model=get_model(models, request.GET.get("model"))

        fields=model._meta.fields

        form=CSVFileUploadForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            df=pd.read_csv(request.FILES["file"])

            vcolumns=validate_columns(df, fields)

            if vcolumns != True:
                errors["columns"]=f"Your CSV Don't have column {vcolumns}!"
            else:

                import_data = {
                    "csv_file_name" : request.FILES["file"].name,
                    "model" : model.__name__,
                }

                import_ = ImportCSV.objects.create(**import_data)

                pdcols={}

                df=df.where(pd.notnull(df), None)

                for column in fields:
                    pdcols[column.name]=df[column.name].to_list()

                import_csv_data_to_db.delay(import_.id, pdcols, model.__name__)

                return HttpResponse(f"<h1> Importing! <br> CSV ID = {import_.id}</h1>")

        context["columns"]=fields
        context["form"]=form
#        context["model"] = model

    context["errors"]=errors


    return render(request, "import.html", context)


@ staff_member_required
def export_view(request):

    models=apps.get_models()

    if not request.GET.get("model") or not request.GET.get("model") in list(map(lambda model: model.__name__, models)):
        return HttpResponse("<h1>Model Name isn't Corent!</h1>")

    else:

        model = get_model(models, request.GET.get("model"))

        fields = []

        for field in model._meta.fields:
            fields.append(field.name)

        name = "media/exports/export-" + ''.join(secrets.choice(string.ascii_letters) for i in range(6)) + ".csv"

        response = HttpResponse(content_type="text/csv")

        response['Content-Disposition'] = f'attachment; filename="{name}"'

        writer = csv.writer(response)

        writer.writerow(fields)

        for object in model.objects.values():
            writer.writerow(list(map(lambda obj: str(obj[-1]), object.items())))
        
    return response