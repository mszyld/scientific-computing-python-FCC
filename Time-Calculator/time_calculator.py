def convert_time_to_24 (time):
  if time[1] == ":":
    hours = int(time[0:1])
  else:
    hours = int(time[0:2])
  if time[-2] == "P" and hours != 12:
    hours += 12
  minutes = int(time[-5:-3])
  return (hours,minutes)

def convert_time_to_12 (hours,minutes):
  if hours == 12:
    return "12:" + str(minutes).zfill(2) + " PM"
  if hours == 0:
    return "12:" + str(minutes).zfill(2) + " AM"
  ans = str(hours%12) + ":" + str(minutes).zfill(2)
  if hours > 12:
    return ans + " PM"
  return ans + " AM"
  
def add_time(start, duration, day=""):
  DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
  hours,minutes = convert_time_to_24(start)
  duration_as_list = duration.split(":")
  hours += int(duration_as_list[0])
  minutes += int(duration_as_list[1])
  hours += minutes//60
  minutes = minutes%60
  new_time = convert_time_to_12(hours%24,minutes)
  if day:
    new_day = (DAYS.index(day.lower())+hours//24)%7
    new_time += ", " + DAYS[new_day].capitalize()
  if hours >= 24:
    if hours < 48:
      new_time += " (next day)"
    else:
      new_time += " (" + str(hours//24) + " days later)"
  return new_time
