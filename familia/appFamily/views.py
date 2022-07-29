from django.shortcuts import render
from appFamily.models import Family



def create_family(request):
    person = Family.objects.create(name = 'Patricia', last_name = 'Miranda', age = 50, dni = 35565374)
    context = {
        'person': person
    }
    return render(request, 'template_person.html',context=context)

def all_family(request):
    family = Family.objects.all()
    context ={
        'family': family

    }
    return render(request, 'family_list.html', context=context)