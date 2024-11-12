from django.shortcuts import render
from django.views import    View



class HomeView(View):
    templates_name='index.html'

    def get(self,request):
        return render(request,self.templates_name)