# Generated by Django 3.2.5 on 2021-08-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='academic_documents',
            field=models.FileField(blank=True, default='DEFAULT VALUE', null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='student',
            name='academic_level',
            field=models.CharField(blank=True, choices=[('1', 'Bachelors'), ('2', 'Diploma'), ('3', 'Certificate'), ('4', 'High School Diploma')], default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='admission_date',
            field=models.DateField(blank=True, default='DEFAULT VALUE', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='district',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email_address',
            field=models.EmailField(blank=True, default='DEFAULT VALUE', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Binary')], default='DEFAULT VALUE', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='medical_form',
            field=models.FileField(blank=True, default='DEFAULT VALUE', null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='student',
            name='natioinal_id',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, choices=[('1', 'Rwandan'), ('2', 'Kenyan'), ('3', 'Ugandan'), ('4', 'SouthSudanese'), ('5', 'Sudanes')], default='DEFAULT VALUE', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='DEFAULT VALUE', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default='DEFAULT VALUE', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default='DEFAULT VALUE', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=12, null=True),
        ),
    ]