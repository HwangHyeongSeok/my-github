from django.views.generic.base import TemplatesView

class HomeView(TemplatesView):
    template_name ='home.html'