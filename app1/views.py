from django.shortcuts import render
from .models import List_Jobs, Python, Command, Sysadmin, Latest
import lotocheck


def home(request):
	pyt = Python.objects.values()
	com = Command.objects.values()
	sys = Sysadmin.objects.values()
	job = List_Jobs.objects.values()
	lo = ""
	if request.method == 'POST':
		n = str(request.POST.get("num1"))
		lo = lotocheck.check(n)


	return render(request, 'home.html', {'pyts': pyt, 'coms': com, 'syss': sys, 'jobs': job, 'lo': lo})