from django import forms

class VideoForm(forms.ModelForm):

    title = forms.CharField(
        max_length=200,
        widget = forms.TextInput(
            attrs={'class':'form-input',
                   'placeholder':'Video Title'
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class':'form-input',
                   'placeholder':'Video Description',
                   'rows':'4'
            }
        )
    )
    video_file = forms.FileField(
        widget=forms.FileInput(attrs={
            'class':'form-input',
            'accept':'video/*'
        })
    )

    def clean_video_file(self):
        video = self.cleaned_data.get('video_file')
        if video:
            if video.size > 100 * 1024 * 1024:
                raise forms.ValidationError("Video must be less than 100MB")

            allowed_types = ['video/mp4', 'video/webm', 'video/quicktime', 'video/x-msvideo']
            if video.content_type not in allowed_types:
                raise forms.ValidationError("Video must be one of {}".format(allowed_types))

        return video
