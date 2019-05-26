# -*- coding: utf-8 -*-
from django import forms


class NewComplaint(forms.Form):
    """
        This is form for new complaint
    """
    title = forms.CharField(label=u'Тема жалобы', max_length=100)
    text = forms.CharField(label=u'Текст жалобы', widget=forms.Textarea)


