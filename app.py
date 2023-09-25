from flask import Flask, request
import mysql_helper

app = Flask(__name__)


def _find_next_id():
    return max(country["id"] for country in countries) + 1


@app.get("/countries")
def get_countries():
    columns, items = mysql_helper.sql_select("Countries")
    columns_names = get_columns_names(columns)
    countries = []
    for item in items:
        country = get_table_entry(columns_names, item)
        countries.append(country)
    return countries, 200


@app.get("/countries/<id_id>")
def get_country(id_id):
    columns, item = mysql_helper.sql_select("Countries", f"Id = {id_id}")
    columns_names = get_columns_names(columns)
    country = get_table_entry(columns_names, item.all()[0])
    return country, 200


@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be json"}, 415


def get_columns_names(columns):
    columns_names = [].copy()
    for column in columns.all():
        columns_names.append(column[0])
    return columns_names


def get_table_entry(columns_names, row_values):
    table_entry = {}.copy()
    for iteration in range(len(columns_names)):
        table_entry[columns_names[iteration]] = row_values[iteration]
    return table_entry
