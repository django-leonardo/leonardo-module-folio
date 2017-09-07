# -*- coding: UTF-8 -*-

from django.template.response import SimpleTemplateResponse
from django.shortcuts import render
from leonardo_module_folio.models import (Category, CategoryTranslation, Client,
                                          Project, ProjectTranslation)


def category_detail(request, category_slug=None):
    object = CategoryTranslation.objects.get(slug=category_slug).parent
    category_list = Category.objects.filter(active=True, parent=None)
    context = {
        'object': object,
        'category_list': category_list,
        'in_appcontent_subpage': True
    }
    return render(request, 'folio/category_detail.html', context)


def project_list(request):
    category_list = Category.objects.filter(active=True, parent=None)
    client_list = Client.objects.filter(active=True)
    object_list = Project.objects.filter(active=True)
    context = {
        'object_list': object_list,
        'client_list': client_list,
        'xx': 'xxxxxx',
        'category_list': category_list,
        'in_appcontent_subpage': True
    }
    return render(request, 'folio/project_list.html', context)


def project_detail(request, category_slug=None, project_slug=None):
    object = ProjectTranslation.objects.get(slug=project_slug).parent
    category_list = Category.objects.filter(active=True, parent=None)
    return render(request,
        'folio/project_detail.html',
        {
            'object': object,
            'category_list': category_list,
            'in_appcontent_subpage': True
        }
    )
