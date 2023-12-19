import json

seconds = 0

with open('2.json') as users:
    d = json.load(users)
    for user in d['users']:
        for poge in user['poges']:
            for song in poge['songs']:
                time = song['length'].split(":")
                seconds += (int(time[0]) * 60)
                seconds += int(time[1])

fminutes = seconds//60
fhours = (seconds//60) // 60
fdays = (seconds//60) // 60 // 24

print(f'{seconds} seconds of poge')
print(f'{fminutes} minutes and {seconds - (fminutes * 60 )} seconds')
print(f'{fhours} hours and {fminutes - (fhours * 60)} minutes and {seconds - (fminutes * 60)} seconds')
print(f'{fdays} days and {fhours - (24 * fdays)} hours and {fminutes - (fhours * 60)} minutes and {seconds - (fminutes * 60)} seconds')
print(f'{seconds / 60 / 60 / 24} days of poge')               