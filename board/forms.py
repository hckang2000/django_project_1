from django import forms

class BoardForm (forms.Form):
    title = forms.CharField(error_messages = {'required': "제목를 입력해주세요"},
    label = "제목", max_length=128)
    contents = forms.CharField(widget= forms.Textarea, 
    error_messages = {'required': "내용을 입력해주세요"}, 
    label = "내용")
    tags = forms.CharField(required = False, label = "태그")
