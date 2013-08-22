# -*- coding: utf-8 -*-
from django import forms
class RequirementForm(forms.Form):
	description=forms.CharField(max_length=10000,widget=forms.Textarea)
	scifactor=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0',"id":"appendedInput",'class':'span2'}))
	prize=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0','class':'span2'}))