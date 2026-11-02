import time

wait_time = 1
retries = 5
attempts = 1

while attempts <= retries:
    print("Attempt", attempts, "wait-time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
