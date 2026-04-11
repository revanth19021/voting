from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from .models import Candidate,Election,Vote

from django.contrib.auth.decorators import login_required

def election_list(request):
    elections=Election.objects.all()
    
    return render(request,'election_list.html',{'elections':elections})

def candidate_list(request,election_id):
    election=get_object_or_404(Election,id=election_id)
    candidates=Candidate.objects.filter(election=election)
    
    return render(request,'candidate_list.html',{
        'election':election,
        'candidates':candidates
    })
    
@login_required
def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    election = candidate.election
    user = request.user

    # ❌ check if already voted
    if Vote.objects.filter(user=user, election=election).exists():
        return render(request, 'candidate_list.html', {
            'election': election,
            'candidates': Candidate.objects.filter(election=election),
            'error': 'You have already voted!'
        })

    
    Vote.objects.create(
        user=user,
        candidate=candidate,
        election=election
    )

    return redirect('election_list')