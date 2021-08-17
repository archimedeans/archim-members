from django.db import models

# Standard college abbreviations 
# see https://www.admin.cam.ac.uk/reporter/2016-17/special/04/section1.shtml
COLLEGES = (
    ("CAI",  "Gonville & Caius"),
    ("CTH",  "St Catherine's"),
    ("CHR",  "Christ's"),
    ("CHU",  "Churchill"),
    ("CL",  "Clare"),
    ("CLH", "Clare Hall"),
    ("CC",  "Corpus Christi"),
    ("DOW",  "Downing"),
    ("ED",  "St Edmund's"),
    ("EM",  "Emmanuel"),
    ("F",  "Fitzwilliam"),
    ("G",  "Girton"),
    ("HO",  "Homerton"),
    ("HH",  "Hughes Hall"),
    ("JE",  "Jesus"),
    ("JN",  "St John's"),
    ("K",  "King's"),
    ("LC",  "Lucy Cavendish"),
    ("M",  "Magdalene"),
    ("MUR",  "Murray Edwards"),
    ("N",  "Newnham"),
    ("PEM",  "Pembroke"),
    ("PET",  "Peterhouse"),
    ("Q",  "Queens'"),
    ("R",  "Robinson"),
    ("SE",  "Selwyn"),
    ("SID",  "Sidney Sussex"),
    ("TH",  "Trinity Hall"),
    ("T",  "Trinity"),
    ("W",  "Wolfson"),
    ("DAR", "Darwin"),
    ("NA", "N/A")
)

class Member(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    crsid = models.CharField(max_length=8)
    alternative_email = models.CharField(max_length=35, null=True, blank=True)
    college = models.CharField(max_length=6, choices = COLLEGES, blank=True)
    life_member = models.BooleanField()
    membership_start = models.DateField()
    membership_end = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.firstname.capitalize()} {self.lastname.capitalize()} ({self.crsid.lower()})'
