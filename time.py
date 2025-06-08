import time
my_Time = int(input("Enter the Time in seconds: "))
              
for counter in range(my_Time, 0, -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600) 
    print(f"Time Left: {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("⏲️⏲️ TIME'S UP ⏲️⏲️")
