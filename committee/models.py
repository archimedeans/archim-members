from django.db import models
from members.models import COLLEGES

class Committee(models.Model):
    """Represents a whole committee for a given year, e.g. 2021-2022."""
    start_year = models.PositiveIntegerField(help_text="The starting year of the committee")
    current = models.BooleanField(default=False)

    def __str__(self):
        return f'Committee ({self.start_year} - {self.start_year + 1})'

class CommitteeMember(models.Model):
    """Represents an individual committee member."""
    index = models.PositiveSmallIntegerField(help_text="Ordering to use on the website")
    position = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=6, choices=COLLEGES, blank=True)
    email = models.CharField(max_length=100, null=True)
    is_publications = models.BooleanField(default=False)
    photo = models.CharField(max_length=100, null=True)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)

    class Meta:
        ordering = ['index']
    
    def __str__(self):
        return f'{self.position} ({self.committee.start_year}): {self.name}, {self.college}'
