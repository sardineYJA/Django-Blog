from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from blog.views import CommonViewMixin
from .models import Link

# Create your views here.

'''function view'''


def links(request):
    return HttpResponse('links')


'''class-base view'''


# 显示友链
class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
