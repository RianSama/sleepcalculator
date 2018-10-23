# Import modules
import datetime


# Have user define variables
age = int(input("How many years old are you? "))
wake = int(input("At what hour would you like to wake? "))
lastmeal = int(input("How many hours ago did you last eat? "))
lastusage = int(input("How many hours ago did you last use a electronic device? "))
lastexercise = int(input("How many hours ago did you last exercise? "))


if age < 8:
    sleep = 12
    if lastexercise <= 1:
        sleep = sleep + 1
        if lastmeal or lastusage <= 2:
            sleep = sleep + 2

elif age >= 8 and age < 12:
    sleep = 10
    if lastexercise <= 1:
        sleep = sleep + 1
        if lastmeal <= 2 or lastusage <= 2:
            sleep = sleep + 2

elif age >= 18:
    sleep = 8
    if lastexercise <= 1:
        sleep = sleep + 1
        if lastmeal or lastusage <= 2:
            sleep = sleep + 2


sleeptime = int(datetime.timedelta(hours = wake - sleep).seconds / 3600)


print("{} hours of sleep is optimal for you.".format(sleep))
print("You should go to sleep at {} hours to wake up at {} hours with optimal sleep.".format(sleeptime, wake))
