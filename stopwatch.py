import time


#input "START" to start the timing
print('Welcome to StopWatch, input "START" to start the timing')
while True:
  userInput=input()
  if userInput.lower()=='start':
    break
  else:
    print('Please input "START" to start the timing')

#start timing
userStartTiming=time.time()
lap=0
lapDict={}
print('Your timing has already started, press ENTER to count laps. Press X to end the timing.')
while True:
  userInput=input()
  if userInput=='':
    lap+=1
    lapKey='Lap '+str(lap)
    lapDict[lapKey]=time.ctime()
    print(lapKey,'-',lapDict[lapKey])
  elif userInput.lower()=='x':
    print('Your timing has stopped, here\'s your result')
    break
  else:
    print('Invalid input! Press ENTER to count laps. Press X to end the timing.')
    continue


for i in lapDict:
  print(i,'-',lapDict[i])




