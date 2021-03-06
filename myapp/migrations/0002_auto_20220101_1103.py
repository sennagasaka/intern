# Generated by Django 3.1 on 2022-01-01 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/noimage.png', upload_to='uploads'),
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talk', models.TextField()),
                ('time', models.DateTimeField()),
                ('talk_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talk_from', to='myapp.user')),
                ('talk_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talk_to', to='myapp.user')),
            ],
        ),
    ]
