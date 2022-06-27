weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

res=filter(lambda day: day if len(day)==6 else "",weekdays)

for day in res:
    print(day)