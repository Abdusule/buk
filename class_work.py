print('HOW MANY KILOMETER DID YOU CYCLE TODAY ?')

kms = input() #Get User Input

miles = float(kms)/1.660934 #Converting from string tp float and divide

miles = round(miles, 2) #Round Result

print(f'Your {kms}km Ride Was {miles}Ml')