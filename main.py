import pyautogui
import time
import requests

def send_request(available_taps, count, token):
    """
    Send a request to the API to log or process taps.

    Parameters:
    available_taps (int): Number of taps available.
    count (int): Number of taps made.
    token (str): Authorization token for the API.

    Returns:
    dict or None: Parsed JSON response or None if the response is invalid.
    """
    url = "https://example.com/api"  # Replace with your API endpoint
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {
        "available_taps": available_taps,
        "count": count,
    }

    response = requests.post(url, json=data, headers=headers)

    # Debugging: Print the response details
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)

    try:
        return response.json()
    except ValueError:
        print("Error: Invalid JSON response")
        return None

def auto_tap(interval, duration, energy_cap, token):
    """
    Auto tap (mouse click) at the current mouse position with energy cap and API logging.

    Parameters:
    interval (float): Time between clicks in seconds.
    duration (float): Total duration for the auto tapping in seconds.
    energy_cap (int): Maximum number of taps before waiting.
    token (str): Authorization token for the API.
    """
    print("Starting auto tap... Move your mouse to the target position.")
    time.sleep(3)  # Give user time to position the mouse
    print("Auto tapping in progress. Press Ctrl+C to stop.")

    start_time = time.time()
    tap_count = 0  # Count the number of taps

    try:
        while time.time() - start_time < duration:
            if tap_count < energy_cap:
                pyautogui.click()  # Perform a click
                tap_count += 1
                time.sleep(interval)  # Wait for the next click
            else:
                print("Energy cap reached! Waiting for 2 minutes...")
                response = send_request(energy_cap, tap_count, token)
                if response:
                    print("API Response:", response)
                else:
                    print("Failed to log data to the server.")
                time.sleep(120)  # Wait for 2 minutes
                tap_count = 0  # Reset tap count after resting
                print("Resuming auto tapping...")
    except KeyboardInterrupt:
        print("\nAuto tapping stopped by user.")
    print("Finished auto tapping.")

# Settings
tap_interval = 0.5  # Seconds between each click
tap_duration = 600  # Total duration in seconds (e.g., 10 minutes)
energy_cap = 1000   # Maximum number of taps before waiting
api_token = "your_api_token_here"  # Replace with your API token

auto_tap(tap_interval, tap_duration, energy_cap, api_token)
