# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import InputForm
from .models import InputModel
import json

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            #Take data from the initial form
            name_input = form.cleaned_data['name0']
            #Convert to json type
            data = json.dumps(name_input,ensure_ascii=False)
            #Create object
            InputModel.objects.create(data=data,field='name0')

            #Loop take data from other form
            for count in range(1,len(request.POST)-1):
                query = 'name' + str(count)
                input_value = request.POST[query]
                #Check for empty field
                if input_value:
                    data = json.dumps(input_value,ensure_ascii=False)
                    field = json.dumps(query)
                    InputModel.objects.create(data=data,field=field)
                count += 1
        return redirect('/done/')
    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form})

def done(request):
    #Take data from the db
    query = InputModel.objects.all().values('id','field','data')
    json_list = list(query)
    return render(request, 'done.html', {'json_list' : json_list})
