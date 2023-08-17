from django.db import models

class Problem(models.Model):
    problem_statement = models.TextField()
    is_solved = models.BooleanField(default=False)
    correct_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.problem_statement