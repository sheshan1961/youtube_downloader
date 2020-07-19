from django import forms

FORMAT = [
    ('m4a', 'mp3'),
    ('mp4', 'mp4'),
]


class UrlForm(forms.Form):
    video_link = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': "input", 'type': "text", 'name': "video", 'autocomplete': "off", 'autofocus': ""}),
        max_length=43, label="")
    video_type = forms.ChoiceField(
        required=True, widget=forms.RadioSelect(attrs={'id': 'listLabels'}), choices=FORMAT, label=""
    )
