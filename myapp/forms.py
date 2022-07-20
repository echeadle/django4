from django import forms
# from urllib import request

class UploadFileForm(forms.Form):
   # Name = request.POST.get('name')
    file = forms.FileField()

def upload_file_exists(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            return True
        else:
            return False 