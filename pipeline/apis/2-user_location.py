#!/usr/bin/env python3
"""
Script to fetch the location of a GitHub user from the GitHub API.
"""

import sys
import requests
from datetime import datetime


def get_user_location(api_url):
    """
    Fetch and print the location of a GitHub user from the provided API URL.
    
    Handles various scenarios such as:
    - User found with a location
    - User not found (404)
    - Rate limiting (403)
    
    Parameters:
        api_url (str): The full GitHub API URL to fetch user data.
    """
    try:
        # Send a GET request to the API URL
        response = requests.get(api_url)

        # Status code 200: Request successful, parse the location
        if response.status_code == 200:
            user_data = response.json()
            location = user_data.get("location")
            if location:
                print(location)
            else:
                print("Location not available")

        # Status code 404: User not found
        elif response.status_code == 404:
            print("Not found")

        # Status code 403: Rate limit exceeded
        elif response.status_code == 403:
            reset_time = int(response.headers.get("X-RateLimit-Reset"))
            current_time = datetime.now().timestamp()
            minutes_to_reset = (reset_time - current_time) // 60
            print(f"Reset in {int(minutes_to_reset)} min")

        # Other status codes: Print error
        else:
            print(f"Error: {response.status_code}")

    except requests.RequestException as e:
        # Handle network or request-related errors
        print(f"Error: {e}")


if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub_API_URL>")
        sys.exit(1)

    # Get the API URL from the command-line argument
    api_url = sys.argv[1]

    # Call the function to fetch and print the user location
    get_user_location(api_url)
