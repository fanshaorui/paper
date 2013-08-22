# -*- coding: utf-8 -*-
from django import forms
from paper.locals import *
class RequirementForm(forms.Form):
	description=forms.CharField(max_length=10000,widget=forms.Textarea,error_messages=description_error_messages)
	scifactor=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0',"id":"appendedInput",'class':'span2'}),error_messages=scifactor_error_messages)
	prize=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0','class':'span2'}),error_messages=prize_error_messages)