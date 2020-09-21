from django.db import models

# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length=50)
    max_bench = models.IntegerField()
    max_squat = models.IntegerField()
    max_deadlift = models.IntegerField()
    max_ohp = models.IntegerField()
    days_worked = models.IntegerField() #potentially replace with date started and use timedelta to find days passed and find week
    def __str__(self):
        return self.account_name + "'s account."

SQUAT = "Squat"
BENCH = "Bench"
DEADLIFT = "Deadlift"
OHP = "Overhead Press"

LIFT_CHOICES = (
    (SQUAT, "Squat"),
    (BENCH, "Bench"),
    (DEADLIFT, "Deadlift"),
    (OHP, "Overhead Press"),
)

class Lift(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    lift_name = models.CharField(max_length=15, choices=LIFT_CHOICES, default=SQUAT)
    lift_date = models.DateField('date')
    reps = models.IntegerField()
    weight = models.IntegerField()
    def __str__(self):
        return self.lift_name + ": " + str(self.reps) + "x" + str(self.weight)