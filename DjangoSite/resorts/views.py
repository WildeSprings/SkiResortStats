from django.http import HttpResponse
from django.template import loader

from .models import ActiveRecord

def index(request):
    resort_list = ActiveRecord.objects.all().order_by('resort_name').values()
    latest_resort = ActiveRecord.objects.latest('last_updated')
    template = loader.get_template('resorts/index.html')
    context = {
        'resort_list': resort_list,
        'latest_resort': latest_resort,
    }
    return HttpResponse(template.render(context, request))
