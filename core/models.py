from django.db import models

class Teacher(models.Model):

    ACADEMIC_DEGREE = [
        ('Specialist','Spe.'),
        ('Master','Me.'),
        ('Doctor','Dr.')
    ]
    name = models.CharField(max_length=200)
    academic_degree = models.CharField(max_length=200,choices=ACADEMIC_DEGREE)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Student(models.Model):

    name = models.CharField(max_length=200)
    matriculation = models.CharField(max_length=200)
    email = models.EmailField()
    leader = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='student_leader')
    coorientator = models.ForeignKey(Teacher,blank=True, null=True,on_delete=models.CASCADE,related_name='student_coorientator')

    def __str__(self):
        return self.name

class Project(models.Model):

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
    name_student = models.OneToOneField(Student,on_delete=models.CASCADE)
    name_project = models.CharField(max_length=1000)
    type_project = models.CharField(max_length=200,choices=TYPE_PROJECT)
    defense_model = models.CharField(max_length=200,choices=DEFENSE_MODEL)


    def __str__(self):
        return self.name_project

class ExaminationBoard(models.Model):
    STATUS = [
        ('Agendada','Agendada'),
        ('Confirmada','Confirmada'),
        ('Concluida','Concluida')
    ]
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    member = models.ManyToManyField(Teacher,related_name="examinationboard_member")
    expected_date = models.DateField()
    expected_time = models.TimeField()
    status = models.CharField(max_length=200,choices=STATUS)
    course_coordinator = models.OneToOneField(Teacher,on_delete = models.DO_NOTHING)

    

    def __str__(self):
        return self.student.name

