from django.contrib import admin

from eshop_sliders.models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'link']
    search_fields = ['name']
    class Meta:
        model = Slider

admin.site.register(Slider, SliderAdmin)