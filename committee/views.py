from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

committee = {
  "year": "2021",
  "committee": [
  {
    "position": "President",
    "name": "Parth Shimpi",
    "college": "Gonville and Caius",
    "email": "president",
    "photo": "parthnew"
  },
  {
    "position": "Vice President",
    "name": "Kathryn Bowers",
    "college": "Magdalene",
    "email": "vice-president",
    "photo": "kathryn"
  },
  {
    "position": "Treasurer",
    "name": "Fong Tsz Lo",
    "college": "Magdalene",
    "email": "junior-treasurer"
  },
  {
    "position": "Events Manager",
    "name": "Nikita Kamath",
    "college": "St Catharine's",
    "email": "events-manager",
    "photo": "nikita"
  },
  {
    "position": "Events Manager",
    "name": "Vishal Gupta",
    "college": "St John's",
    "email": "events-manager",
    "photo": "vishal"
  },
  {
    "position": "External Secretary",
    "name": "Yan Yau Cheng",
    "college": "Magdalene",
    "email": "external-secretary",
    "photo": "yan-yau"
  },
  {
    "position": "Internal Secretary",
    "name": "Ashutosh Tripathi",
    "college": "Emmanuel",
    "email": "internal-secretary"
  },
  {
    "position": "Publicity Officer",
    "name": "Gesa Dünnweber",
    "college": "Gonville and Caius",
    "email": "publicity",
    "photo": "gesa"
  },
  {
    "position": "Sponsorship Officer",
    "name": "Etaash Katiyar",
    "college":"Corpus Christi",
    "email":"corporate-officer"
  },
  {
    "position": "Webmaster",
    "name": "Adam Kelly",
    "college": "Gonville and Caius",
    "email": "webmaster"
  }
  ],
  "publications": [
  {
    "position": "Eureka Editor",
    "name": "Valentin Hübner",
    "college": "Pembroke",
    "email": "eureka-editor"
  }
  ]
}


def index(request):
    template = loader.get_template('committee/index.html')

    return render(request, 'committee/index.html', committee)