# Generated by Django 4.1.3 on 2023-02-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('name', models.CharField(help_text='栏目名称', max_length=150, verbose_name='栏目名称')),
                ('pid', models.IntegerField(default=0, help_text='上级ID', verbose_name='上级ID')),
                ('item_id', models.IntegerField(default=0, help_text='站点ID', verbose_name='站点ID')),
                ('pinyin', models.CharField(help_text='拼音(全拼)', max_length=150, verbose_name='拼音(全拼)')),
                ('code', models.CharField(help_text='拼音(简拼)', max_length=150, verbose_name='拼音(简拼)')),
                ('is_cover', models.IntegerField(default=2, help_text='是否有封面：1是 2否', verbose_name='是否有封面：1是 2否')),
                ('cover', models.CharField(help_text='封面地址', max_length=255, verbose_name='封面地址')),
                ('status', models.IntegerField(choices=[(1, '正常'), (2, '停用')], default=1, help_text='栏目状态：1-正常 2-停用', verbose_name='栏目状态：1-正常 2-停用')),
                ('note', models.CharField(help_text='栏目备注', max_length=255, null=True, verbose_name='栏目备注')),
                ('sort', models.IntegerField(default=0, help_text='栏目排序', verbose_name='栏目排序')),
            ],
            options={
                'verbose_name': '栏目表',
                'verbose_name_plural': '栏目表',
                'db_table': 'django_item_cate',
            },
        ),
    ]
