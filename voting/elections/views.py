from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Candidate, Election, Vote


@login_required
def election_list(request):
    elections = Election.objects.all()
    return render(request, 'election_list.html', {'elections': elections})


@login_required
def candidate_list(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    candidates = Candidate.objects.filter(election=election)

    already_voted = Vote.objects.filter(
        user=request.user,
        election=election
    ).exists()

    return render(request, 'candidate_list.html', {
        'election': election,
        'candidates': candidates,
        'already_voted': already_voted
    })


@login_required
def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    election = candidate.election

    if Vote.objects.filter(user=request.user, election=election).exists():
        return redirect('candidate_list', election_id=election.id)

    Vote.objects.create(
        user=request.user,
        candidate=candidate,
        election=election
    )

    return redirect('election_list')


@login_required
def results(request, election_id):
    if request.user.profile.role != 'admin':
        return HttpResponse("Not allowed")

    election = get_object_or_404(Election, id=election_id)
    candidates = Candidate.objects.filter(election=election)

    results_data = []

    for candidate in candidates:
        count = Vote.objects.filter(candidate=candidate).count()
        results_data.append({
            'candidate': candidate,
            'votes': count
        })

    return render(request, 'results.html', {
        'election': election,
        'results': results_data
    })