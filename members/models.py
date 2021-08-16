from django.db import models

COLLEGES = (
    ("CAIUS",  "Gonville & Caius"),
    ("CATH",  "St Catherine's"),
    ("CHRST",  "Christ's"),
    ("CHUR",  "Churchill"),
    ("CLARE",  "Clare"),
    ("CLAREH", "Clare Hall"),
    ("CORP",  "Corpus Christi"),
    ("DOWN",  "Downing"),
    ("EDM",  "St Edmund's"),
    ("EMM",  "Emmanuel"),
    ("FITZ",  "Fitzwilliam"),
    ("GIRT",  "Girton"),
    ("HOM",  "Homerton"),
    ("HUGH",  "Hughes Hall"),
    ("JESUS",  "Jesus"),
    ("JOHNS",  "St John's"),
    ("KINGS",  "King's"),
    ("LCC",  "Lucy Cavendish"),
    ("MAGD",  "Magdalene"),
    ("NEWH",  "Murray Edwards"),
    ("NEWN",  "Newnham"),
    ("PEMB",  "Pembroke"),
    ("PET",  "Peterhouse"),
    ("QUEN",  "Queens'"),
    ("ROBIN",  "Robinson"),
    ("SEL",  "Selwyn"),
    ("SID",  "Sidney Sussex"),
    ("TRINH",  "Trinity Hall"),
    ("TRIN",  "Trinity"),
    ("WOLFC",  "Wolfson"),
    ("DRWN", "Darwin"),
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
