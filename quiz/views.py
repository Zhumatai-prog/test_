from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login




from .models import *
from .forms import *

def home_view(request):                                     # ok
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('afterlogin')
    return render(request,'navbar.html')


class ProjectLoginView(LoginView):
    template_name = 'quiz/authentication/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home_view')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
     model = User
     template_name = 'quiz/authentication/signup.html'
     form_class = RegisterUserForm
     success_url = reverse_lazy('login')
     success_msg = 'Пользователь создан!'

     def get_success_url(self):
         return self.success_url

     def form_valid(self, form):
         form_valid = super().form_valid(form)
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         aut_user = authenticate(username=username, password=password)
         login(self.request, aut_user)
         return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('home_view')


def student_exam_view(request):
    topics = Topic.objects.all()
    return render(request,'quiz/exam/topic_list.html',{'topics':topics})


def user_view(request):
    users = User.objects.all()
    return render(request,'quiz/exam/user_list.html',{'users':users})


def take_exam_view(request,pk):
    topic = Topic.objects.get(id=pk)
    total_questions = Question.objects.all().filter(topic=topic).count()

    return render(request,'quiz/exam/test_take.html',
                 {'topic':topic,
                  'total_questions':total_questions})


def start_exam_view(request,pk):
    topic = Topic.objects.get(id=pk)
    questions = Question.objects.all().filter(topic=topic)
    answer_ = ''
#    if request.method=='POST':
#        if request.POST:
#            form = QuestionUpdateForm(request.POST, request.FILES)
#            if form.is_valid():
#                form.save()
    response = render(request,'quiz/exam/test_start.html',{'topic':topic,'questions':questions, 'answer_':answer_})
    response.set_cookie('topic_id',topic.id)
    return response

#Model.objects.filter(id = 223).update(field1 = 2)
#class ProductUpdateView(UpdateView):
#    model = Question
#    template_name = 'delivery/products/product_update.html'
#    context_object_name = 'product'
#    fields = '__all__'

#    def get_success_url(self):
#        return reverse_lazy('delivery:product_detail', kwargs={'pk': self.object.pk})

#def add_stuff(bar):
#    item = Item.objects.create(foo=bar)
#    return item

#def specific_add_item_view(request):
#    item = add_stuff(bar)



def calculate_marks_view(request):
    if request.COOKIES.get('topic_id') is not None:
        topic_id = request.COOKIES.get('topic_id')
        topic = Topic.objects.get(id=topic_id)

        total_marks = 0
        questions = Question.objects.all().filter(topic=topic)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer

        student = models.Student.objects.get(user_id = request.user.id)
        result = Result()

        result.exam=topic
        result.student=student
        result.save()

        return HttpResponseRedirect('view-result')
