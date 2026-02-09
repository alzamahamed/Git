import time

for i in range(1, 101):
    print(f"\rLoading {i*1}%", end="")
    time.sleep(1)
