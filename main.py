import os
import time

def auto_tap(x, y, interval, duration, energy_cap):
    """
    Auto tap (simulate screen taps) at the specified coordinates with an energy cap.

    Parameters:
    x (int): X-coordinate for the tap.
    y (int): Y-coordinate for the tap.
    interval (float): Time between taps in seconds.
    duration (float): Total duration for the auto tapping in seconds.
    energy_cap (int): Maximum number of taps before waiting.
    """
    print(f"Starting auto tap at ({x}, {y})...")
    time.sleep(3)  # Give the user time to prepare
    print("Auto tapping in progress. Press Ctrl+C to stop.")

    start_time = time.time()
    tap_count = 0  # Count the number of taps

    try:
        while time.time() - start_time < duration:
            if tap_count < energy_cap:
                # Use Termux API to simulate a tap
                os.system(f"input tap {x} {y}")
                tap_count += 1
                time.sleep(interval)  # Wait for the next tap
            else:
                print("Energy cap reached! Waiting for 2 minutes...")
                time.sleep(120)  # Wait for 2 minutes
                tap_count = 0  # Reset tap count after resting
                print("Resuming auto tapping...")
    except KeyboardInterrupt:
        print("\nAuto tapping stopped by user.")
    print("Finished auto tapping.")

# Settings
tap_x = 500          # X-coordinate for the tap (modify as needed)
tap_y = 500          # Y-coordinate for the tap (modify as needed)
tap_interval = 0.5   # Seconds between each tap
tap_duration = 600   # Total duration in seconds (e.g., 10 minutes)
energy_cap = 1000    # Maximum number of taps before waiting

auto_tap(tap_x, tap_y, tap_interval, tap_duration, energy_cap)
