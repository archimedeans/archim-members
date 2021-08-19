from django.shortcuts import render

from .models import CommitteeMember, Committee

def index(request):
    page_data = { "committee": [], "publications": [] }

    committee = Committee.objects.filter(current=True)
    
    if len(committee) == 0:
      return render(request, 'committee/index.html', {})
    
    page_data["year"] = committee[0].start_year

    committee_members = CommitteeMember.objects.filter(committee_id=committee[0].id)

    for member in committee_members:
      type = "committee" if not member.is_publications else "publications"
      page_data[type].append(member)

    return render(request, 'committee/index.html', page_data)
  
def past(request):
    return render(request, 'committee/past.html')