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
    success_url = reverse_lazy('student')


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

class TeacherListView(generic.ListView):
    def get(self,request):
        teacher_list = Teacher.objects.all()
        return render(request,'teacher_list.html',{'teacher_list':teacher_list})

class TeacherDetailView(generic.DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'

class TeacherUpdateView(generic.UpdateView):
    model = Teacher
    fields = "__all__"
    template_name = "teacher_update.html"
    success_url = reverse_lazy('teacher')

class TeacherDeleteView(generic.DeleteView):
    model = Teacher
    template_name = "teacher_confirm_delete.html"
    success_url = reverse_lazy('teacher')


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

class ProjectListView(generic.ListView):
    def get(self,request):
        project_list = Project.objects.all()
        return render(request,'project_list.html',{'project_list':project_list})

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'

class ProjectUpdateView(generic.UpdateView):
    model = Project
    fields = "__all__"
    template_name = "project_update.html"
    success_url = reverse_lazy('project')

class ProjectDeleteView(generic.DeleteView):
    model = Project
    template_name = "project_confirm_delete.html"
    success_url = reverse_lazy('project')



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


class ExaminationBoardListView(generic.ListView):
    def get(self,request):
        examination_list = ExaminationBoard.objects.all()
        return render(request,'examination_list.html',{'examination_list':examination_list})

class ExaminationBoardDetailView(generic.DetailView):
    model = ExaminationBoard
    template_name = 'examination_detail.html'

class ExaminationBoardUpdateView(generic.UpdateView):
    model = ExaminationBoard
    fields = "__all__"
    template_name = "examination_update.html"
    success_url = reverse_lazy('examination')

class ExaminationBoardDeleteView(generic.DeleteView):
    model = ExaminationBoard
    template_name = "examination_confirm_delete.html"
    success_url = reverse_lazy('examination')
