# Generated by Django 5.0.1 on 2024-02-07 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_answer_answer_answer_choice_choice_score_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'جواب', 'verbose_name_plural': 'جواب ها'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'گزینه', 'verbose_name_plural': 'گزینه ها'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'سوال', 'verbose_name_plural': 'سوال ها'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'تست', 'verbose_name_plural': 'تست ها'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.choice', verbose_name='گزینه'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='examinee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.examinee', verbose_name='شرکت کننده'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.question', verbose_name='سوال'),
        ),
    ]