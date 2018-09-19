from _ast import Global

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import sweetify

from bookphone.forms import SecretariaForm, UnidadForm, PersonalSecretariaForm, PersonalUnidadForm
from bookphone.models import Personal_secretaria, Personal_unidad
from .models import Secretaria, Unidad


def base(request):
    secretarias = Secretaria.objects.order_by('name').all
    return render(request, 'bookphone/base.html', {
        's': secretarias,
        'e_obj': Secretaria,
    })


def list(request, id):
    secretaria = Secretaria.objects.get(id=id)
    personal = Personal_secretaria.objects.filter(secretaria=id).all
    request.session['ids'] = id
    return render(request, 'bookphone/list.html', {
        'se': secretaria,
        'personal': personal,
        'form': SecretariaForm(instance=secretaria),
        'formUnidad': UnidadForm(),
        'formPersonal': PersonalSecretariaForm(),
    })


def nueva_secretaria(request):
    form = SecretariaForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            sweetify.success(request, 'Se ha creado un nueva Secretaria', timer=3000, icon='success')
            return HttpResponseRedirect(reverse('list', args=[post.id]))
        else:
            sweetify.error(request, 'Ha ocurrido un error', persistent=':(', timer=3000, icon='error')
    else:
        form = SecretariaForm()
    return render(request, 'bookphone/nueva_secretaria.html', {'form': form})


def edit_secretaria(request, id):
    secretaria = Secretaria.objects.get(id=id)
    if request.method == 'POST':
        form = SecretariaForm(request.POST, request.FILES, instance=secretaria)
        if form.is_valid():
            save = form.save()
            sweetify.success(request, 'Se ha modificado una Secretaria', timer=3000, icon='success')
            return HttpResponseRedirect(reverse('list', kwargs={'id': secretaria.id}))
        else:
            sweetify.error(request, 'Ha ocurrido un error', persistent=':(', timer=3000, icon='error')
            print(str(form))
    else:
        form = SecretariaForm(instance=secretaria)
    return render(request, 'bookphone/edit_secretaria.html', {
        'secre': secretaria,
        'form': form,
        'agency_obj': Secretaria
    })


def delete_secretaria(request, id):
    secretaria = Secretaria.objects.get(id=id)
    secretaria.delete()
    sweetify.success(request, 'Se ha eliminado una Secretaria', timer=3000, icon='success')
    return HttpResponseRedirect(reverse('base'))


def personal_secretaria(request, id):
    ids = request.session['ids']
    personal = Personal_secretaria.objects.get(id=id)
    secretaria = Secretaria.objects.get(id=ids)
    return render(request, 'bookphone/personal.html', {
        'personal': personal,
        'se': secretaria,
        'form': PersonalSecretariaForm(instance=secretaria),
    })


def nuevo_personal_secre(request):
    form = PersonalSecretariaForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            sweetify.success(request, 'Se ha creado nuevo personal en Secretaria', timer=3000, icon='success')
            return HttpResponseRedirect(reverse('personal-secretaria', args=[post.id]))
        else:
            sweetify.error(request, 'Ha ocurrido un error', persistent=':(', timer=3000, icon='error')
            print(str(form))
    else:
        form = PersonalSecretariaForm()


def edit_personal_secretaria(request, id):
    personal_secre = Personal_secretaria.objects.get(id=id)
    if request.method == 'POST':
        form = PersonalSecretariaForm(request.POST, request.FILES, instance=personal_secre)
        if form.is_valid():
            save = form.save()
            sweetify.success(request, 'Se ha modificado los datos', timer=3000, icon='success')
            return HttpResponseRedirect(reverse('list', kwargs={'id': personal_secre.id}))
        else:
            sweetify.error(request, 'Ha ocurrido un error', persistent=':(', timer=3000, icon='error')
            print(str(form))
    else:
        form = PersonalSecretariaForm(instance=personal_secre)
    return render(request, 'bookphone/editar_personal_secretaria.html', {
        'personal': personal_secre,
        'form': form,
    })


def delete_personal_secretaria(request, id):
    persona = Personal_secretaria.objects.get(id=id)
    persona.delete()
    ids = request.session['ids']
    sweetify.success(request, 'Se ha eliminado un Personal', timer=3000, icon='success')
    return HttpResponseRedirect(reverse('list', args={ids}))



def unidad(request, id):
    request.session['idu'] = id
    ids = request.session.get('ids')
    secretaria = Secretaria.objects.get(id=ids)
    unidad = Unidad.objects.get(id=id)
    personal_uni = Personal_unidad.objects.filter(unidad=id).all
    return render(request, 'bookphone/unidad.html', {
        'un': unidad,
        'se': secretaria,
        'personal_u': personal_uni,
        'form': UnidadForm(instance=unidad),
        'formPersonal': PersonalUnidadForm(),
    })



def nueva_unidad(request):
    form = UnidadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            sweetify.success(request, 'Se ha creado un nueva Unidad', timer=3000, icon='success')
            return HttpResponseRedirect(reverse('unidad', args=[post.id]))
        else:
            sweetify.error(request, 'Ha ocurrido un error', persistent=':(', timer=3000, icon='error')
            print(str(form))
    else:
        form = UnidadForm()


def edit_unidad(request, id):
    unidad = Unidad.objects.get(id=id)
    if request.method == 'POST':
        form = UnidadForm(request.POST, request.FILES, instance=unidad)
        if form.is_valid():
            save = form.save()
            sweetify.success(request, 'Se ha modificado una Unidad', timer=3000, icon='success')
            return HttpResponseRedirect(reverse('list', kwargs={'id': unidad.id}))
        else:
            sweetify.error(request, 'Ha ocurrido un error', persistent=':(', timer=3000, icon='error')
            print(str(form))
    else:
        form = UnidadForm(instance=unidad)
    return render(request, 'bookphone/edit_unidad.html', {
        'uni': unidad,
        'form': form,
    })


def delete_unidad(request, id):
    unidad = Unidad.objects.get(id=id)
    unidad.delete()
    ids = request.session['ids']
    # print(id)
    return HttpResponseRedirect(reverse('list', args={ids}))


def personal_unidad(request, id):
    idu = request.session['idu']
    personal_uni = Personal_unidad.objects.get(id=id)
    ids = request.session['ids']
    secretaria = Secretaria.objects.get(id=ids)
    unidad = Unidad.objects.get(id=idu)
    return render(request, 'bookphone/personal_unidad.html', {
        'personal_uni': personal_uni,
        'uni': unidad,
        'se': secretaria,
    })


def nuevo_personal_unidad(request):
    form = PersonalUnidadForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            sweetify.success(request, 'Se ha creado nuevo personal en Unidad', timer=3000, icon='success')
            return HttpResponseRedirect(reverse('personal-unidad', args=[post.id]))
        else:
            sweetify.error(request, 'Ha ocurrido un error', persistent=':(', timer=3000, icon='error')
            print(str(form))
    else:
        form = PersonalUnidadForm()
