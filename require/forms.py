# -*- coding: utf-8 -*-
from django import forms
from paper.locals import *
class RequirementForm(forms.Form):
	theme=forms.CharField(max_length=140,widget=forms.TextInput(attrs={'placeholder':'请输入论文的主题'}),error_messages=theme_error_messages)
	description=forms.CharField(max_length=10000,widget=forms.Textarea,error_messages=description_error_messages)
	scifactor=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0',"id":"appendedInput",'class':'span2'}),error_messages=scifactor_error_messages)
	prize=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0','class':'span2'}),error_messages=prize_error_messages)
	circle_min=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0','class':'span1'}),error_messages=circle_error_messages)
	circle_max=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'0','class':'span1'}),error_messages=circle_error_messages)
	