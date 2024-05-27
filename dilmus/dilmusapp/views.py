from django.shortcuts import render
print ("view ishladi")
# Create your views here.
def index(request):
    print('ss')
    return render(request, 'index.html')
        