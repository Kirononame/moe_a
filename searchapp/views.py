from django.shortcuts import render
from searchapp.utils import userProfile
import json

def search_view(request):
    context = {}
    if request.method == 'POST':
        try:
            # Get the NIN value from the form (ensure it's an integer)
            nin = int(request.POST.get('nin', ''))
            if nin:
                # Call the userProfile API with the provided NIN
                profile_data = userProfile(nin)
                formatted_profile_data = json.dumps(profile_data, indent=4, ensure_ascii=False)  # Beautify the JSON response and handle non-ASCII characters
                context['profile_data'] = formatted_profile_data
        except ValueError:
            # If NIN is not a valid integer, handle the error
            context['error'] = "Invalid NIN format. Please enter a valid number."
    return render(request, 'searchapp/search.html', context)

