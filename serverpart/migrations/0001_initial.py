# Generated by Django 4.2.5 on 2023-09-15 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(choices=[('Часть 1', 'Часть 1'), ('Часть 2', 'Часть 2')], max_length=10)),
                ('section', models.IntegerField(choices=[(1, 'Арифметика'), (2, 'Алгебра'), (3, 'Геометрия')])),
                ('theme', models.CharField(choices=[('00', 'Без темы'), ('01', 'Числа простые и составные. Разложение числа на простые множители. Делитель и кратное. Признаки делимости чисел. Наибольший общий делитель, наименьшее общее кратное. '), ('02', 'Рациональные числа. Свойства арифметических действий.'), ('03', 'Иррациональные выражения. Арифметический корень, действия с корнями. '), ('04', 'Арифметические действия с положительными и отрицательными числами. '), ('05', 'Обыкновенные дроби. Арифметические действия с обыкновенными дробями. Представление обыкновенных дробей десятичными дробями.'), ('06', 'Отношение. Пропорции. Проценты.'), ('07', 'Степень с натуральным и целым показателями. Квадратный корень. '), ('08', 'Приближенные значения величин. Округление чисел. '), ('09', 'Числовые неравенства и их свойства.'), ('10', 'Тождественные преобразования алгебраических выражений.'), ('11', 'Выражения, содержащие модуль. '), ('12', 'Алгебраическая дробь. Действия с алгебраическими дробями.'), ('13', 'Свойства степени с целым показателем. '), ('14', 'Свойства арифметического квадратного корня. Преобразование выражений, содержащих квадратные корни.'), ('15', 'Многочлены. Действия с многочленами. Формулы сокращенного умножения. Разложение многочленов на множители. '), ('16', 'Логарифмы, их свойства. Тождественные преобразования логарифмических и показательных выражений. '), ('17', 'Уравнения алгебраические, логарифмические, показательные, тригонометрические, иррациональные. '), ('18', 'Системы двух линейных уравнений с двумя переменными.'), ('19', 'Неравенства и их свойства. '), ('20', 'Функция. Способы задания функции. Область определения функции. '), ('21', 'Графики элементарных функций и их свойства.'), ('22', 'Свойства параллельных и перпендикулярных прямых. '), ('23', 'Треугольник.'), ('24', 'Виды треугольников. Свойства сторон и углов треугольника. '), ('25', 'Теорема Пифагора. Синус, косинус, тангенс острого угла. Решение прямоугольных треугольников. '), ('26', 'Четырехугольники. '), ('27', 'Окружность и круг. Центральные и вписанные углы. Окружность, вписанная в треугольник. Окружность, описанная около треугольника. '), ('28', 'Длина окружности, площадь круга. '), ('29', 'Площадь и периметр треугольника и четырехугольника. '), ('30', 'Площадь боковых поверхностей цилиндра, конуса, шара. Площадь сферы.'), ('31', 'Площади поверхностей призмы и пирамиды. '), ('32', 'Формулы объемов прямоугольного параллелепипеда, прямой призмы, пирамиды, цилиндра, конуса, шара. '), ('33', 'Декартовы координаты на плоскости.'), ('34', 'Декартовы координаты в пространстве.'), ('35', 'Движение.'), ('36', 'Осевая симметрия. Центральная симметрия.')], default='00', max_length=2)),
                ('difficulty', models.IntegerField(choices=[(0, 'Любая сложность'), (1, 'Легкий'), (2, 'Средний'), (3, 'Тяжелый')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_image', models.ImageField(blank=True, null=True, upload_to='task_images/')),
                ('solution_image', models.ImageField(blank=True, null=True, upload_to='solution_images/')),
                ('answer_text', models.TextField(blank=True, null=True)),
                ('task_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serverpart.taskkeys')),
            ],
        ),
        migrations.CreateModel(
            name='SolvedTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serverpart.tasks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
