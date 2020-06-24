# Generated by Django 3.0.7 on 2020-06-24 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200623_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinationboard',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='coorientator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_coorientator', to='core.Teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_leader', to='core.Teacher'),
        ),
    ]