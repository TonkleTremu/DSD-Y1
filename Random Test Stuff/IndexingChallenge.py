screen_times = [120, 95, 140, 160, 80, 100, 200]
print(screen_times[2]) # Prints screen time for day 3

total = 0
for x in range(0, 3): # Finds average of first 3 days.
    total += screen_times[x]
print(f"The average is {total/3:.2f}")

screen_times.pop(-1) # Replaces last value with new value.
screen_times.append(int(input("New value:\n")))

print(f"The highest and lowest values are {max(screen_times)} and {min(screen_times)} respectively") # Displays highest and lowest values.