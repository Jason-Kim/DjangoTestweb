# -*- coding:utf-8 -*-
'''
Created on 2016. 11. 24.

@author: mskim
'''

class PagingHelper:
    "paging helper class"
    def get_page_list(self, total_cnt, rows_per_page):               
        if ((total_cnt % rows_per_page) == 0):
            self.num_pages = total_cnt / rows_per_page;
            print 'getTotalPage #1'
        else:
            self.num_pages = (total_cnt / rows_per_page) + 1;
            print 'getTotalPage #2'
               
        self.total_page_list = []
        for j in range( self.num_pages ):
            self.total_page_list.append(j+1)
                
        return self.total_page_list        

    def __init__(self ):
        self.num_pages = 0
        self.total_page_list  = 0