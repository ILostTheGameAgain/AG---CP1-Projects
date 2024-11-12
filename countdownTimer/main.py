#Alec George Raid: countdown timer

#will ask user for integer for seconds, minutes, and hours, will count down, display values
import time

#set variables
hours = -1
minutes = -1
seconds = -1
hour_display = ""
minute_display = ""
second_display = ""

#function for user input
def timer_time(scale):
  try:
    time_value = int(input(f"\nhow many {scale} would you like to add to the timer? (type integer, 0 for none): "))
  except ValueError:
    return -1
  return time_value

#while loop to set hours
while True:
  hours = timer_time("hours")
  if hours >= 0:
    break
  else:
    print("\ninvalid input")

#while loop to set minutes
while True:
  minutes = timer_time("minutes")
  if minutes >= 0 and minutes < 60:
    break
  else:
    print("\ninvalid input")

#while loop to set seconds
while True:
  seconds = timer_time("seconds")
  if seconds >= 0 and seconds < 60:
    break
  else:
    print("\ninvalid input")

#timer display and count down
print("\n")
while True:
  #make look a little nicer
  if len(str(hours)) == 1:
    hour_display = f"0{hours}"
  else:
    hour_display = hours

  if len(str(minutes)) == 1:
    minute_display = f"0{minutes}"
  else:
    minute_display = minutes

  if len(str(int(seconds))) == 1:
    second_display = f"0{seconds}"
  else:
    second_display = seconds
    
  print(f"{hour_display} : {minute_display} : {second_display}")
  #count down, every 10th of a second, go down by 0.1
  time.sleep(0.1)
  
  seconds = round(seconds-0.1, 1)
  if seconds < 0:
    seconds = 59
    minutes -= 1
  if minutes < 0:
    minutes = 59
    hours -= 1
  if hours < 0:
    break

for x in range(10):
  print("times up!")