weather = (1,0,0,0,1,2,0,2)
sunny = 0
rainy = 0
spring = 0
for i in range(0,7):
    if(weather[i]==0):
        rainy+=1
    elif(weather[i]==1):
        sunny+=1
    else:
        spring+=1

if(rainy>sunny):
    if(rainy>spring):
        print("Good Weather")
    else:
        print("Very Good Weather")
else:
    if(sunny>spring):
        print("Very Hot Weather. Please take an Umbrella with you if you go out from your home.")
    else:
        print("Very Good Weather")