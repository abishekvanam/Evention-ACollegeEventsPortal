from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect

def mypythonfunction(request,a):
    return render(request,'forum/ind.html',{'a':a})