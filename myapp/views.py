import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Inputs


def index(request):
    if request.method == 'POST':
        result = dict(request.POST)
        result.pop('csrfmiddlewaretoken')
        for k, v in result.items():
            result[k] = v[0]
        my_json = json.dumps(result)
        new_input = Inputs(data=my_json)
        new_input.save()
        return HttpResponseRedirect(reverse('myapp:all_data'))
    return render(request, 'myapp/index.html')


def all_data(request):
    my_dict = {'result': []}
    for data in Inputs.objects.all():
        my_json = json.loads(str(data))
        my_dict['result'].append(my_json)
    return JsonResponse(my_dict)
