# Generated by Django 4.1 on 2024-04-10 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
            ],
        ),
    ]
