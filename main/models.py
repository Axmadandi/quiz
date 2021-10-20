from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField("Ismi", max_length=150)
    surname = models.CharField("Familiya", max_length=150)
    tel_num = models.PositiveIntegerField("telfon raqami")

    TIME = [
        ('ERTALABKI','ertalabki'),
        ('KECHKI','kechki'),
    ]
    times = models.CharField(choices=TIME, max_length=150, blank=True)
    true_a = models.ManyToManyField("main.Quizzes", related_name="user_true")
    false_a = models.ManyToManyField("main.Quizzes", related_name="user_false")
    
    def __str__(self):
        return self.name
    

class Ways(models.Model):
    name = models.CharField("Nomi", max_length=150)
    icon = models.CharField("Icon fontaosem", max_length=50)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.name
    

class Answers(models.Model):
    title = models.CharField("Javob", max_length=550, blank=True)
    image = models.ImageField("rasmi", upload_to="answers_img/", blank=True)
    true_or_false = models.BooleanField("togrimi")

    def __str__(self):
        return self.title
    

class Quizzes(models.Model):
    title = models.CharField("Savol", max_length=2150)
    ways = models.ForeignKey("main.Ways", related_name="way_quizz", on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answers, related_name="ans_quizz")

    def __str__(self):
        return self.title
