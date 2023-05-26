from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request,"index.html")


def iletisim_view(request):
    return render(request, 'iletisim.html')

def purchase_view(request):
    return redirect('purchase_success')

def purchase_success_view(request):
    return render(request, 'purchase.html')
