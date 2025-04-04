from django.contrib.auth.models import User
from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Ответ вопроса"
        verbose_name_plural = "Ответы вопросов"

    def __str__(self):
        return self.text


class Question(models.Model):
    name = models.CharField(max_length=256)
    answers = models.ManyToManyField(Answer, verbose_name="ответы", related_name="answers")
    right_answers = models.ManyToManyField(Answer, verbose_name="правильные ответы", related_name="right_answers")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.name

class TestCase(models.Model):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField(Question, verbose_name="вопросы", related_name="questions")

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.name

class TestCaseResults(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, verbose_name="тест", related_name="test_case", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name="вопрос", related_name="question", on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, verbose_name="ответ", related_name="answer", on_delete=models.CASCADE)
    is_right = models.BooleanField()

    class Meta:
        verbose_name = "Результаты теста"
        verbose_name_plural = "Результаты тестов"

    def __str__(self):
        return f"{self.user.username} - {self.test_case.name}"


class Theme(models.Model):
    name = models.CharField(max_length=512)
    test_cases = models.ManyToManyField(TestCase, verbose_name="тесты", related_name="test_cases")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.name
