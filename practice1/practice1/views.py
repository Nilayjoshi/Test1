#MY_CUSTOMIZE_VIEWS #NILAY
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'nilay','place':'Jupiter'}
    return render(request,'index.html', params)
    # return HttpResponse("""<a href="https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm">Django</a>Good Good""")

def about(request):
    return HttpResponse("Hello World About US Page <a href='/'>Back</a>")

def getdata(request):
    # Get the text
    text = request.POST.get('name','No Data')
    Boolean = request.POST.get('active','off')
    upper = request.POST.get('upper','off')
    print(text)
    print(upper)
    if(Boolean == 'on'):
        analyzed = ""
        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for val in text:
            if val not in punc:
                analyzed += val      
        print(analyzed)
        params = {'purpose':'For passing data','analyzed_text': analyzed}
        text = analyzed
        # return render(request,'passdata.html', params)
    if(upper == 'on'):
        analyzed = ""
        for val in text:
            analyzed += val.upper()
        params = {'purpose':'For Upper Case','letters': analyzed}
        text = analyzed
        # return HttpResponse(analyzed)
    if(Boolean != "on" and upper != "on"):
        return HttpResponse("Error")
    return render(request, 'passdata.html', params)     
    # Shown the next page
    # return HttpResponse("Hello World About US Page <a href='/'>Back</a>")