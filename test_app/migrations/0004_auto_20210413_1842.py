# Generated by Django 2.2.4 on 2021-04-13 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_login_app', '0003_remove_user_user_name'),
        ('test_app', '0003_auto_20210413_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='comment_likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to='user_login_app.User'),
        ),
        migrations.AlterField(
            model_name='like',
            name='message_likes',
            field=models.ManyToManyField(blank=True, related_name='messages_likes', to='user_login_app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user_login_app.User'),
        ),
    ]
