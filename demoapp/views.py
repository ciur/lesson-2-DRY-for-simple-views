from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    # index page for everyone
    # call some models here
    # filter, order them and add to context

    return render(
        request, 'demoapp/index.html'
    )


class PageView(TemplateView):
    pass
