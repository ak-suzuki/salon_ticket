from django.views.generic import View
from django.shortcuts import HttpResponse


class TestView(View):
    def get(self, request):
        print(99)
        import datetime
        return HttpResponse(f"Hello world!{datetime.datetime.now()}")
