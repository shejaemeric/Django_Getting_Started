from django.shortcuts import render,get_object_or_404
from .models import Meeting
# Create your views here.

def getMeeting(request,id):
    """get one meeting detail based on id

    Args:
        request (req): requests sent by client agent
        id (int): meeting Id
    """
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request,"meetings/details.html",
                  {
                      "meeting":meeting
                  })
