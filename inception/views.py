from typing import Any
from django.db import models
from django.shortcuts import render
from django.views import generic
from .models import Problem
from .constants import CONSTANTS
from django.http import HttpResponse

class IndexView(generic.DetailView):
    template_name = 'inception/index.html'
    context_object_name = 'index_problem_statement'

    def get_queryset(self):
        return Problem.objects.get(id=CONSTANTS.INDEX_PROBLEM_ID)

def problems(request):
    return HttpResponse("Problems page")

def hiccup(request, problem_id):
    return HttpResponse("particular problem %s. " % problem_id)

def result(request, problem_id):
    return HttpResponse("result page %s. " % problem_id)