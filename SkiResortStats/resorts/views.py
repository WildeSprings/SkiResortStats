from django.http import HttpResponse
from django.template import loader

from .models import ActiveRecord

def index(request):
    resort_list = ActiveRecord.objects.all
    template = loader.get_template('resorts/index.html')
    context = {
        'resort_list': resort_list,
    }
    return HttpResponse(template.render(context, request))
