from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from.models import Questions

# Create your views here.
def index(request):
    myname = "Bảo Hưng"
    taisan = ["Điện thoại", "máy tính", "máy bay", "nhiều tiền"]
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html", context)

def view_list(request):
    #get_object_or_404(Questions, pk=5)
    list_question = Questions.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Questions.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})

def vote(request, question_id):
    q = Questions.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        return HttpResponse("Lỗi không có choice")
    c.vote = c.vote +1
    c.save()
    return render(request, "polls/result.html", {"q": q})
