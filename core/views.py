from django.shortcuts import render
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.views import generic
from .models import Teacher,Student,Project,ExaminationBoard
from .forms import ExaminationBoardRegistrationForm,StudentRegistrationForm,\
    TeacherRegistrationForm,ProjectRegistrationForm



# Create your views here.

class IndexView(generic.ListView):

    def get(self,request):
        examination_board = ExaminationBoard.objects.all()
        return render(request,'index.html',{'examination_board':examination_board})


class StudentRegistrationView(generic.CreateView):

    def get(self,request):
        form  = StudentRegistrationForm()
        return render(request,'student_registration.html',{'form':form})

    def post(self,request):
        form  = StudentRegistrationForm(request.POST)
        if form.is_valid():
            model_instance = Student(**form.cleaned_data)
            model_instance.save()
            return redirect('student')

class StudentListView(generic.ListView):
    def get(self,request):
        student_list = Student.objects.all()
        return render(request,'student_list.html',{'student_list':student_list})

class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'student_detail.html'


class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = "__all__"
    template_name = "student_update.html"
    success_url = reverse_lazy('student')

class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = 'student'


class TeacherRegistrationView(generic.CreateView):
    
    def get(self,request):
        form  = TeacherRegistrationForm()
        return render(request,'teacher_registration.html',{'form':form})

    def post(self,request):
        form  = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            model_instance = Teacher(**form.cleaned_data)
            model_instance.save()
            return redirect('index')



class ProjectRegistrationView(generic.CreateView):
    
    def get(self,request):
        form  = ProjectRegistrationForm()
        return render(request,'project_registration.html',{'form':form})

    def post(self,request):
        form  = ProjectRegistrationForm(request.POST)
        if form.is_valid():
            model_instance = Project(**form.cleaned_data)
            model_instance.save()
            return redirect('index')


class ExaminationBoardRegistrationView(generic.CreateView):
    
    def get(self,request):
        form  = ExaminationBoardRegistrationForm()
        return render(request,'examination_registration.html',{'form':form})

    def post(self,request):
        form  = ExaminationBoardRegistrationForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
        
            
            examination_board = ExaminationBoard(
                student = dados_form['student'],            
                expected_date = dados_form['expected_date'],
                expected_time = dados_form['expected_time'],
                status = dados_form['status'],
                course_coordinator = dados_form['course_coordinator']
            )
            examination_board.save()    
            members = Teacher.objects.filter(id__in=request.POST.getlist('member'))
            if members:
                for member in members:
                    examination_board.member.add(member)


            return redirect('index')
        else:
            
            return HttpResponse('invalido')