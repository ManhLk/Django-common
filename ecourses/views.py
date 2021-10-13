from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'School': 'HUST',
        'Name': 'ManhLK'
    }
    return render(request = request, template_name='test.html', context= data)