from django.forms import CharField, Form


class SearchForm(Form):
    query = CharField(max_length=100) 