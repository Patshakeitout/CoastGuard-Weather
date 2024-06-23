from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, 'index.html')
    

class TeamView(View):
    def get(self, request):
        
        return render(request, 'team.html')