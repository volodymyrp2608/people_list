from django.shortcuts import render, get_object_or_404
from .models import List_People
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import ListPeopleForm

def data_people(request):
    people = List_People.objects.all()
    return render(request, 'people/list_people/people_list.html', {'people': people})

def person_create(request):
    form = ListPeopleForm()
    context = {'form': form}
    html_form = render_to_string('people/includes/partial_person_create.html', context, request=request, )
    return JsonResponse({'html_form': html_form})

def person_update(request, pk):
    person = get_object_or_404(List_People, pk=pk)
    form = ListPeopleForm(instance=person)
    context = {'form': form}
    html_form = render_to_string('people/includes/partial_person_update.html', context, request=request, )
    return JsonResponse({'html_form': html_form})

def person_delete(request, pk):
    person = get_object_or_404(List_People, pk=pk)
    context = {'person': person}
    html_form = render_to_string('people/includes/partial_person_delete.html', context, request=request, )
    return JsonResponse({'html_form': html_form})

def updated_list(request):
    data = dict()
    people = List_People.objects.all()
    data['html_people_list'] = render_to_string('people/list_people/partial_people_list.html', {'people': people})
    return JsonResponse(data)
