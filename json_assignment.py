# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 19:52:50 2026

@author: Naveen
"""

#-------------------------------
#Task 1 — Build a JSON Structure
#-------------------------------

import json  # Import the built-in JSON module for serialization/deserialization

# Define a Python dictionary representing a user profile
user_profile={
    "name":"someone",
    "age":45,
    "email":"someone@something.com",
    "is_active":True,
    "skills":["Limitless","Domain Expansion","Domain Amplification","Simple Domain","Reversed Curse Technique"]
    }

# Convert the Python dictionary to a JSON-formatted string with indentation for readability
user_profile_json=json.dumps(user_profile,indent=1)

# Print the JSON string to the console
print(user_profile_json)

#-------------------------------
#Task 2 — Parse an API Response
#-------------------------------

# Simulated API response as a JSON string
API_response='{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

# Parse (deserialize) the JSON string into a Python dictionary
API_response_dict=json.loads(API_response)

# Extract the 'username' from the nested 'data' object
username=API_response_dict["data"]["username"]

# Extract the 'score' from the nested 'data' object
score=API_response_dict["data"]["score"]

# Print the username
print(f"username: { username }")

# Print the score
print(f"score: { score }")

# Print a formatted summary message combining extracted values
print(f"User { username } scored { score } points")

#-------------------------------
#Task 3 — Handle Nested JSON
#-------------------------------


# Create a nested JSON string from a Python dictionary
nested_json=json.dumps(
    {
      "name": "Priya",
      "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "zip": "560001"
      }
    }
)

# Parse the JSON string back into a Python dictionary to modify or access its values
nested_json_dict=json.loads(nested_json)

# Print specific nested values: city and ZIP code from the address object
print(f"city: {nested_json_dict['address']['city']}")
print(f"zip code: {nested_json_dict['address']['zip']}")

# Add a new key-value pair ('country': 'India') inside the nested 'address' object
nested_json_dict["address"]["country"]="India"

# Convert the updated dictionary back into a formatted JSON string with indentation
nested_json=json.dumps(nested_json_dict,indent=4)

# Print the updated nested JSON structure
print(nested_json)


