from django.shortcuts import render, HttpResponse
import os

path = 'E:\\shanu\\marathi\\assets\\www'



# Create your views here.
def index(request):
    context={
        'variable':'shanu'
    }
    return render(request, 'index.html', context)


def filefun(request):
    context={
        'variable':'shanu'
    }
    if request.method=='GET':
           print("======================>shanu")
           
           
           print(request.GET.getlist('data')[0])
           if not os.path.exists(path):
                  os.makedirs(path)

           filename = 'shanu' + '.txt'
           with open(os.path.join(path, filename), 'w',encoding="utf-8") as temp_file:
                temp_file.write(request.GET.getlist('data')[0])
                return HttpResponse('hello hi how are you')

def createapp(request):
    print("createapp")
    os.chdir( 'E:\\shanu\\marathi' )
    os.system('cmd /k "gradlew build"')
    return HttpResponse('hello hi how are you')