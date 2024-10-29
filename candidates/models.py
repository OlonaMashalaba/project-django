from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    party = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.party})"
def add(a, b):
    """Adds two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

