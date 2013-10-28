# Create your views here.
from django.http import HttpResponse
from slider.models import *
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from lfs.caching.utils import lfs_get_object_or_404
from lfs.core.models import Shop

def slide(request):
    obj = Slider.objects.all()
    all_img =[]
    for i in range(len(obj)):
        all_img.append(obj[i])
    template = loader.get_template('lfs/slider/slider.html')
    context = RequestContext(request, {
        'first_img':all_img[:-1],
        'last_img':all_img[-1],
        'all_img':all_img,
        'obj':obj,
    })
    return HttpResponse(template.render(context))
"""
def index(request):
    obj = Slider.objects.all()
    all_img =[]
    for i in range(len(obj)):
        all_img.append(obj[i])
    shop = lfs_get_object_or_404(Shop, pk=1)
    return render_to_response('lfs/shop/shop.html', RequestContext(request, {
        "shop":shop,
        'first_img':all_img[:-1],
        'last_img':all_img[-1],
        'all_img':all_img,
        'obj':obj,
    }))
    """
