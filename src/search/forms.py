'''
Created on 2016. 11. 25.

@author: mskim
'''

from django import forms

class PostForm(forms.Form):
    reference = forms.CharField(label='reference', max_length=1024, required=False)
    search_title = forms.CharField(label='search title', max_length=2048, required=False)
    search_data = forms.CharField(label='search data', max_length=1024*50)
    
    
class GetForm(forms.Form):
    current_page = forms.IntegerField(label='current page')