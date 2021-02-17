from django import forms
from ckeditor.widgets import CKEditorWidget


class GossipForm(forms.Form):
    text = forms.CharField(label="", widget=CKEditorWidget(config_name='gossip'),
                           error_messages={'required': '评论内容不能为空'})
