from django.shortcuts import render
from .models import SiteSetting

def siteSetting_page(request):
    
    siteSetting = SiteSetting.objects.first()

    context = {
        'siteSetting':siteSetting
    }

    return render(request, 'site_setting.html', context)