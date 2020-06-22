from .models import Teacher,Student,Project
from django import forms


class TeacherRegistrationForm(forms.Form):

    ACADEMIC_DEGREE = [
        ('Specialist','Spe.'),
        ('Master','Me.'),
        ('Doctor','Dr.')
    ]
    name = forms.CharField(max_length=200,label='Name',required=True)
    academic_degree = forms.ChoiceField(choices=ACADEMIC_DEGREE,widget=forms.Select(),required=True)
    email = forms.EmailField(label='Email',required=True)    

class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=200,label='Name')
    matriculation = forms.CharField(max_length=200,label='Matriculation')
    email = forms.EmailField(label='Email')
    leader = forms.ModelChoiceField(queryset=Teacher.objects.all(),empty_label=None)
    coorientator = forms.ModelChoiceField(queryset=Teacher.objects.all(),empty_label=None,required=False)

class ProjectRegistrationForm(forms.Form):
    TYPE_PROJECT = [
    ('TCC','TCC'),
    ('TCC1','TCC1'),
    ('TCC2','TCC2')
]
    DEFENSE_MODEL = [
    ('Monography','Monography'),
    ('Article','Article'),
    ('SoftwareReport','Software Report'),
    ('Others','Others')
]
    name_student = forms.ModelChoiceField(queryset=Student.objects.all())
    name_project = forms.CharField(max_length=400, label = "Name project")
    type_project = forms.ChoiceField(choices=TYPE_PROJECT,widget=forms.Select(),required=True)
    defense_model = forms.ChoiceField(choices=DEFENSE_MODEL,widget=forms.Select(),required=True)


class ExaminationBoardRegistrationForm(forms.Form):
    STATUS = [
        ('Agendada','Agendada'),
        ('Confirmada','Confirmada'),
        ('Concluida','Concluida')
    ]
    student = forms.ModelChoiceField(queryset = Student.objects.all())
    member = forms.ModelMultipleChoiceField(queryset = Teacher.objects.all())
    expected_date = forms.DateField(widget = forms.DateInput())
    expected_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    status = forms.ChoiceField(choices=STATUS,widget=forms.Select(),required=True)
    course_coordinator = forms.ModelChoiceField(queryset = Teacher.objects.all())   