from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .pdfSplitter import splitFile
import os, time


def home(request):

	splitted_file_url = None

	if request.method == 'POST' and request.FILES['fileName']:
		uploadedFile = request.FILES['fileName']

		start = int(request.POST.get('from'))
		end = int(request.POST.get('to'))

		fs = FileSystemStorage()

		old_file = fs.save(uploadedFile.name, uploadedFile)
		old_file_url = fs.url(old_file)

		splitted_file = splitFile( F"../pdfSplitter/media{old_file_url}", start = start, end = end)

		old_file_url = fs.url(old_file)
		splitted_file_url = fs.url(splitted_file)

		context = {'splitted_file_url' : splitted_file_url, 'splitted_file_name': splitted_file}

		return render(request, 'splitter/index.html', context)

	context = {'splitted_file_url' : splitted_file_url}
	
	return render(request, 'splitter/index.html', context)