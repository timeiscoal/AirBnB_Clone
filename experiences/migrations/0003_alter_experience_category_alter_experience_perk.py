# Generated by Django 4.1.3 on 2022-11-20 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        ('experiences', '0002_experience_category_alter_experience_end_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiences', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='perk',
            field=models.ManyToManyField(related_name='experiences', to='experiences.perk'),
        ),
    ]
