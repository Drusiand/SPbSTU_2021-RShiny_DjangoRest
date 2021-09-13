from django.db import models


class GameUnit(models.Model):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    DIFFICULTY_CHOICES = [
        (EASY, EASY),
        (MEDIUM, MEDIUM),
        (HARD, HARD)
    ]
    name = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES)
    content = models.TextField(max_length=500)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
