from django.shortcuts import render
from django.http import HttpResponse
import json
from .mykernel import chatbot_graph

# init the bot
print('chatbot init started ......')
handler = chatbot_graph.ChatBotGraph()
print('chatbot init finished ......')

# Create your views here.
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def home(request):
    return render(request, 'home.html')

def answer(request):
    if request.method == 'POST':
        question = request.POST.get('question', "感冒")
        print('用户提问：%s'%question)
        if question == "quit":
            answer = "Byebye"
        answer = handler.chat_main(question)
        print('智障回答：%s' % answer)
        answer_dict = {'ans': answer}
        return HttpResponse(json.dumps(answer_dict), content_type='application/json')