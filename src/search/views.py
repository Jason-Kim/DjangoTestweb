# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

from .models import *
from search.paging_helper import PagingHelper
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm, GetForm
from solr_request import search as solr_search
import re


ROWS_PER_PAGES = 10
reg_idkipi = re.compile('^[A-Z]{2}[0-9]+[A-Z0-9]{1,2}_[0-9]{8}[ \t\n]*$', re.IGNORECASE)

def report(request):
    if request.method=="GET":
        form = GetForm(request.GET)
        if form.is_valid()==False:     # first call report page 
            current_page = 1
            report_list = Report.objects.all()[:ROWS_PER_PAGES]
            num_report = Report.objects.all().count()
            
            paging = PagingHelper()
            total_page_list = paging.get_page_list( num_report, ROWS_PER_PAGES)
            print 'total_page_list', total_page_list
        else:
            current_page = get_cleaned_data(form.cleaned_data, 'current_page')
            num_report = Report.objects.all().count()                  
            
            print 'current_page=', current_page
                
            # 페이지를 가지고 범위 데이터를 조회한다
            report_list = Report.objects.all()[(current_page-1)*ROWS_PER_PAGES : current_page*ROWS_PER_PAGES]
        
        # 전체 페이지를 구해서 전달...
        paging = PagingHelper();
        total_page_list = paging.get_page_list( num_report, ROWS_PER_PAGES)
        print 'total_page_list', total_page_list
        
        return render(request, 'report.html', {'report_list': report_list, 'num_report': num_report,
                                               'current_page':current_page ,'total_page_list':total_page_list} )
    else:
        pass

def search(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #print form.cleaned_data['search_data']
            #search_results = [{'id_kipi':"123", "tl":form.cleaned_data['search_data'], "score":0.94},
            #                 {'id_kipi':"456", "tl":form.cleaned_data['search_data'], "score":0.94},
            #                 {'id_kipi':"789", "tl":form.cleaned_data['search_data'], "score":0.94}]
            
            search_title = get_cleaned_data(form.cleaned_data, 'search_title').strip()
            search_data = get_cleaned_data(form.cleaned_data, 'search_data').strip()
            
            if reg_idkipi.search(search_data) == None and len(search_title) > 0:
                search_data = "(%s)^2.0 OR (%s)^1.0" % (search_title, search_data)

            search_results = solr_search(search_data.encode('utf-8'))
            
            reference = get_cleaned_data(form.cleaned_data, 'reference').strip()
            if reference != None:
                reference = reference.splitlines()

            return render(request, 'search.html', {'search_results':search_results, 'reference':reference})
    else:
        return render(request, 'search.html', {'search_results':[]})

def get_cleaned_data(cleaned_data, name, defval=None):
    if cleaned_data.get(name) != None:
        return cleaned_data.get(name)
    else:
        return defval
