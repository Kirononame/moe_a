# searchapp/utils.py

import requests
from .consts import userprofile_url, headers

def userProfile(nin: int):
    data = {
    "retrieveUserMOEQualificationsRequest": {
        "body": {
          "nin": f"{nin}"
        }
    }
}
 
    
    
    try:
        # Make the POST request using the constants from consts.py
        response = requests.post(userprofile_url, json=data, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for 4xx/5xx responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
