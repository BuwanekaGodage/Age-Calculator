#This is to calculate your time left to stay alive aprox

print("Please enter your Name and your age")
name = input('Name:')
print('What is your age?',name)
age = int(input('age:'))
days = age * 365
minutes = age * 525948
seconds = age * 1556926
left_days = (55 * 365) - age
years_left = (left_days/365)
print(name,'has been alive for',days,'days',minutes,'minutes',seconds,'seconds')
print("How many days do you have left to live (average age is 70)")
print(left_days)
print('thank you',name,'for using my little age calculation software..')
print ('Creator, Buwaneka Widhurinda Godage')
