# -*- coding: utf-8 -*-
from django.http import HttpResponse
# view for index page
def page(request):
    return HttpResponse("Hello world!")
