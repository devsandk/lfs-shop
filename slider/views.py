# Create your views here.
from django.http import HttpResponse
from slider.models import *
from django.template import RequestContext, loader

def slide(request):
    obj = Slider.objects.all()
    all_img =[]
    counter=['0']
    for i in range(len(obj)):
        all_img.append(obj[i])
        counter.append(str(int(counter[-1])+1))
    counter=counter[:-1]
    template = loader.get_template('lfs/slider/slider.html')
    context = RequestContext(request, {
        'first_img':all_img[:-1],
        'last_img':all_img[-1],
        'all_img':all_img,
        'counter':counter[:-1],
        'counter_last':counter[-1],
        'obj':obj,
    })
    return HttpResponse(template.render(context))
