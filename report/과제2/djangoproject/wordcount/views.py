from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] # 글 원문, 전체를 뜻하게 됨
    words = text.split() # 잘라져서 list로 저장됨
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary:
            #increse
            word_dictionary[word]+=1

        else:
            #add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full' : text, 'total' : len(words), 'dictionary' : word_dictionary.items()})