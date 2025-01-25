import pyautogui
import time

def auto_tap(interval, duration, energy_cap):
    """
    Auto tap (mouse click) at the current mouse position with energy cap.

    Parameters:
    interval (float): Time between clicks in seconds.
    duration (float): Total duration for the auto tapping in seconds.
    energy_cap (int): Maximum number of taps before waiting.
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

auto_tap(tap_interval, tap_duration, energy_cap)
