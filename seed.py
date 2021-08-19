import os
import datetime
import django

COLLEGES = (
    ("CAI",  "Gonville & Caius"),
    ("CTH",  "St Catharine's"),
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

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archim.settings')
django.setup()

# from members.models import Member
from committee.models import Committee, CommitteeMember


college_lookup = {}

for college in COLLEGES:
    college_lookup[college[1]] = college[0]


COMMITTEES = [
{
  "year": "2017",
  "committee": [
  {
    "position": "President",
    "name": "Yanni Du",
    "college": "Pembroke",
    "email": "president",
    "photo": "president",
    "description": "I’m a third year mathmo at Pembroke college and my interests lie in probability and statistics. When I’m not doing maths I enjoy running, climbing and playing with Doug the dog. Also puns! One of my favourite puns/ jokes is: &quot;What do you call a male submerged swimmer who swims away exponentially?&quot; &quot;Diver-gent!&quot;"
  },
  {
    "position": "Vice President",
    "name": "Yash Patel",
    "college": "Pembroke",
    "email": "vice-president",
    "description": "too cool"
  },
  {
    "position": "External Secretary",
    "name": "Eve Pound",
    "college": "Murray Edwards",
    "email": "secretary"
  },
  {
    "position": "Internal Secretary",
    "name": "Diogo Fonseca",
    "college": "Pembroke",
    "email": "secretary",
    "description": "easily triggered by differing opinions on memes or music"
  },
  {
    "position": "Treasurer",
    "name": "Joe Needham",
    "college": "Pembroke",
    "email": "junior-treasurer",
    "photo": "treasurer",
    "description": "I'm Joe, the Treasurer, and I'm a second year mathmo at Pembroke. Whem I'm not failing to complete an example sheet, I enjoy playing football, running, and looking at pictures of my dogs."
  },
  {
    "position": "Publicity Officer",
    "name": "Zheneng Xie",
    "college": "Magdalene",
    "email": "publicity",
    "description": "Hi! I'm Zheneng, a third year mathmo with an interest in Analysis and Statistics. When not studying I enjoy mystery novels and jogging. I'll be popping up a lot in your inboxes so please read my emails, and I'll hopefully see you at one of our events!"
  },
  {
    "position": "Events Manager",
    "name": "Jin Choi",
    "college": "Pembroke",
    "email": "events-manager",
    "description": "naively pretentious"
  },
  {
    "position": "Events Manager",
    "name": "Yuen Ng",
    "college": "Trinity",
    "email": "events-manager",
    "photo": "yuen.jpg",
    "description": "Hi - I'm Yuen, a third year mathmo with a taste for creating and solving both puzzles and crossnumbers. Things that I like doing include: learning languages, seeing shows/concerts in Cambridge, catching up with friends, and occasionally playing piano."
  },
  {
    "position": "Corporate Officer",
    "name": "Vanessa Guo",
    "college": "Queens'",
    "email": "corporate-officer",
    "photo": "corporate",
    "description": "I am a third year Mathmo from Queens' college. My main interest lies in probability and statistics but I also quite enjoy Analysis and methods. Apart from  having fun in contemplating Maths problems, I like traveling and in particular good food with good friends along the way!"
  },
  {
    "position": "Webmaster",
    "name": "Dexter Chua",
    "college": "Robinson",
    "email": "webmaster",
    "photo": "webmaster.png",
    "description": "I'm a fourth year mathematician, mostly interested in category theory, geometry and type theory. I also have some side interests in physics and programming. I also enjoy hiking during my free time, but unfortunately Cambridge is too flat for that."
  },
  {
    "position": "General Member",
    "name": "Marc Isern",
    "college": "Christ's"
  },
  {
    "position": "General Member",
    "name": "Kevin Lin",
    "college": "King's",
    "photo": "kevin",
    "description": "Hi, I'm Kevin from King's. Yes, I know these information are already available the line above, but this is what happens when you are too lazy to write something and asks someone else to do it for you."
  },
  {
    "position": "General Member",
    "name": "Valentin H&uuml;bner",
    "college": "Pembroke",
    "description": "impulsive"
  },
  {
    "position": "General Member",
    "name": "Josh Osborne",
    "college": "Pembroke",
    "description": "intimidating"
  },
  {
    "position": "General Member",
    "name": "Tim Colpus",
    "college": "Pembroke"
  },
  {
    "position": "General Member",
    "name": "Jeremy Taylor",
    "college": "Pembroke",
    "description": "things go over his head"
  },
  {
    "position": "General Member",
    "name": "Jonathan Lewis-Brown",
    "college": "Pembroke"
  }
  ],
  "publications": [
  {
    "position": "Eureka Editor",
    "name": "Michael Grayling",
    "college": "Sidney Sussex",
    "email": "eureka-editor"
  },
  {
    "position": "Eureka Assistant Editor",
    "name": "Oliver Feng",
    "college": "Trinity",
    "email": "eureka-asst-editor"
  },
  {
    "position": "Eureka Assistant Editor",
    "name": "Robert Allen",
    "college": "Homerton",
    "email": "eureka-asst-editor"
  },
  {
    "position": "Eureka Assistant Editor",
    "name": "James Hodge",
    "college": "King's",
    "email": "eureka-asst-editor"
  }
  ]
},
{
  "year": "2018",
  "committee": [
  {
    "position": "President",
    "name": "Yash Patel",
    "college": "Pembroke",
    "email": "president",
    "photo": "yash"
  },
  {
    "position": "Vice President",
    "name": "Diogo Fonseca",
    "college": "Pembroke",
    "email": "vice-president",
    "photo": "diogo"
  },
  {
    "position": "External Secretary",
    "name": "Lulu Beatson",
    "college": "Murray Edwards",
    "photo": "lulu",
    "email": "secretary"
  },
  {
    "position": "Internal Secretary",
    "name": "Patrick Kennedy-Hunt",
    "college": "St John's",
    "email": "secretary",
    "photo": "patrick"
  },
  {
    "position": "Treasurer",
    "name": "Jin Choi",
    "college": "Pembroke",
    "email": "junior-treasurer",
    "photo": "jin"
  },
  {
    "position": "Publicity Officer",
    "name": "James Bolton",
    "college": "Pembroke",
    "email": "publicity"
  },
  {
    "position": "Sponsorship Officer",
    "name": "Anthony Kattuman",
    "college": "St John's",
    "email": "corporate-officer"
  },
  {
    "position": "Webmaster",
    "name": "Valentin Hübner",
    "college": "Pembroke",
    "email": "webmaster",
    "photo": "valentin"
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
},
{
  "year": "2019",
  "committee": [
  {
    "position": "President",
    "name": "James Bolton",
    "college": "Pembroke",
    "email": "president"
  },
  {
    "position": "Vice President",
    "name": "Jiazheng Zhu",
    "college": "Pembroke",
    "email": "vice-president"
  },
  {
    "position": "Treasurer",
    "name": "Fong Tsz Lo",
    "college": "Magdalene",
    "email": "junior-treasurer"
  },
  {
    "position": "Events Manager",
    "name": "Beth Holmes",
    "college": "Murray Edwards",
    "email": "events-manager"
  },
  {
    "position": "Events Manager",
    "name": "Shavindra Jayasekera",
    "college": "Trinity",
    "email": "events-manager"
  },
  {
    "position": "External Secretary",
    "name": "Andy Zhao",
    "college": "Trinity",
    "email": "external-secretary",
    "photo": "andy"
  },
  {
    "position": "Internal Secretary",
    "name": "Matthew Wearden",
    "college": "St Catharine's",
    "email": "internal-secretary"
  },
  {
    "position": "Publicity Officer",
    "name": "Parth Shimpi",
    "college": "Gonville & Caius",
    "email": "publicity",
    "photo": "parth"
  },
  {
    "position": "Sponsorship Officer",
    "name": "Michael Norman",
    "college": "Pembroke",
    "email": "corporate-officer"
  },
  {
    "position": "Webmaster",
    "name": "Valentin Hübner",
    "college": "Pembroke",
    "email": "webmaster",
    "photo": "valentin"
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
},
{
  "year": "2020",
  "committee": [
  {
    "position": "President",
    "name": "Parth Shimpi",
    "college": "Gonville & Caius",
    "email": "president",
    "photo": "parth"
  },
  {
    "position": "Vice President",
    "name": "Matthew Holland",
    "college": "Magdalene",
    "email": "vice-president"
  },
  {
    "position": "Treasurer",
    "name": "Fong Tsz Lo",
    "college": "Magdalene",
    "email": "junior-treasurer"
  },
  {
    "position": "Events Manager",
    "name": "Gar Jun Chim",
    "college": "Selwyn",
    "email": "events-manager"
  },
  {
    "position": "Events Manager",
    "name": "Vedanshu Mahajan",
    "college": "Selwyn",
    "email": "events-manager"
  },
  {
    "position": "External Secretary",
    "name": "Yuriy Tumarkin",
    "college": "Trinity",
    "email": "external-secretary"
  },
  {
    "position": "Internal Secretary",
    "name": "Gesa Dünnweber",
    "college": "Gonville & Caius",
    "email": "internal-secretary"
  },
  {
    "position": "Publicity Officer",
    "name": "Julius Villar",
    "college": "Trinity Hall",
    "email": "publicity"
  },
  {
    "position": "Sponsorship Officer",
    "name": "Etaash Katiyar",
    "college":"Corpus Christi",
    "email":"corporate-officer"
  },
  {
    "position": "Webmaster",
    "name": "Vincent Tse",
    "college": "Homerton",
    "email": "webmaster",
    "photo":"vincent"
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
},
{
  "year": "2021",
  "committee": [
  {
    "position": "President",
    "name": "Parth Shimpi",
    "college": "Gonville & Caius",
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
    "college": "Gonville & Caius",
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
    "college": "Gonville & Caius",
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
]

for idx, committee in enumerate(COMMITTEES):
    print(f'Adding Committee {committee["year"]}')

    committee_obj = {
        "start_year": committee["year"]
    }

    com = Committee.objects.create(**committee_obj)

    last_idx = 0

    for idx_u, member in enumerate(committee["committee"]):
        CommitteeMember.objects.create(index=idx_u, position=member["position"], college=college_lookup[member["college"]], email=member.get("email", None), name=member["name"], is_publications=False, photo=member.get("photo", None), committee=com)
        last_idx = idx_u

    for idx_u, member in enumerate(committee["publications"]):
        CommitteeMember.objects.create(index=idx_u + last_idx + 1, position=member["position"], college=college_lookup[member["college"]], email=member.get("email", None), name=member["name"], is_publications=True, photo=member.get("photo", None), committee=com)
        last_idx = idx_u


    print(f'Finished Committee {committee["year"]}')


