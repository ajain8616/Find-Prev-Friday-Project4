from datetime import datetime,timedelta
def findPrevFriday(inpDate):
   weekDay=inpDate.weekday()
   daysToBeReduce=(weekDay+2)%7+1
   prevFridaydate=inpDate-timedelta(days=daysToBeReduce)
   return prevFridaydate
userDateStr =input('Enter Date: ')
userDate=datetime.strptime(userDateStr,'%Y-%m-%d').date()
functioncall=findPrevFriday(userDate)
print('Previous Friday Date:',functioncall)



