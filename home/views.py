from django.shortcuts import render
from django.http import HttpResponse
from .models import Publisher
from django.db.models import Sum, Count
def publisher_list(request):

    data = []

    listViews = Publisher.objects.all().values('page_name').distinct().filter(datepub__range = ("2017-05-10","2017-05-12")).annotate(views=Sum('views'))\
    .annotate(reactions=Sum('reactions')).annotate(comments=Sum('comments')).annotate(shares=Sum('shares')).annotate(videos=Count('page_name'))\
    .order_by('page_name')
    
    for x in listViews:
        data.append(x)

    return render(request, "index.html", {'publisher': data})

def stoyo_list(request):
    perf = Publisher.objects.all()
    return HttpResponse(perf)