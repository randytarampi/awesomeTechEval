from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll

def vote(request, poll_id):
    """
    The logic behind the voting form.

    If you pass it invalid input (i.e. not the XOR of a choice or newChoice) then it spits out a nasty message back at you.
    Otherwise, it leads you to the results page.
    """

    p = get_object_or_404(Poll, pk=poll_id)
    
    if 'choice' in request.POST and len(request.POST['newChoice']) != 0:
       return render_to_response('pollsDetail.html', {
            'poll': p,
            'error_message': "You have to pick/make a choice, a single choice - you can't do both. It's not that hard.",
        }, context_instance=RequestContext(request))
    elif 'choice' in request.POST:
        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the poll voting form.
           return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
    elif len(request.POST['newChoice']) > 0:
        try:
            selected_choice = p.choice_set.get(choice=request.POST['newChoice'])
        except (KeyError, Choice.DoesNotExist):
            new_choice = p.choice_set.create(choice=request.POST['newChoice'], votes=1)
            new_choice.save()
            return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return render_to_response('pollsDetail.html', {
                    'poll': p,
                    'error_message': "Would it kill you to be original?",
                    }, context_instance=RequestContext(request))
    else:
        return render_to_response('pollsDetail.html', {
                    'poll': p,
                    'error_message': "You have to pick or make a choice. It's not that hard.",
                    }, context_instance=RequestContext(request))

def create(request):
    """
    The logic behind the poll creation form.

    Like the voting form, if you pass it some invalid inputs, it screams at you.
    Otherwise, it leads you the poll's detail view.
    """
    
    import datetime
    
    if len(request.POST['question']) == 0 and len(request.POST['choice']) == 0:
	return render_to_response('pollsIndex.html', {
                      	'error_message': "You need to type a choice and question in.", 'latest_poll_list' : Poll.objects.all().order_by('-pub_date')[:5],
                    	}, context_instance=RequestContext(request))
    elif len(request.POST['choice']) == 0:
	return render_to_response('pollsIndex.html', {
                      	'error_message': "You need to type a choice in.", 'latest_poll_list' : Poll.objects.all().order_by('-pub_date')[:5],
                    	}, context_instance=RequestContext(request))
    elif len(request.POST['question']) == 0:
	return render_to_response('pollsIndex.html', {
                      	'error_message': "You need to type a question in.", 'latest_poll_list' : Poll.objects.all().order_by('-pub_date')[:5],
                    	}, context_instance=RequestContext(request))
    else:
    	p = Poll(question=request.POST['question'], pub_date=datetime.datetime.now())
    	p.save()
    	p.choice_set.create(choice=request.POST['choice'], votes=0)
    	return HttpResponseRedirect(reverse('poll_detail', args=(p.id,)))
