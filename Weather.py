# Paris temperature averages
temp_high = {"Jan": 45, "Feb": 46, "March": 54, "April": 61, "May": 68, "June": 73, "July": 77, "Aug": 77, "Sep": 70, "Oct": 61, "Nov": 52, "Dec": 46}
temp_low = {"Jan": 37, "Feb": 37, "March": 41, "April": 45, "May": 52, "June": 57, "July": 61, "Aug": 61, "Sep": 55, "Oct": 50, "Nov": 43, "Dec": 37}
average_temp = {"Jan": 41, "Feb": 43, "March": 48, "April": 52, "May": 59, "June": 61, "July": 68, "Aug": 68, "Sep": 61, "Oct": 54, "Nov": 45, "Dec": 41}
# global variables
yr_temp = sum(average_temp.values())/12
above_average = dict()


def average_paris(month):
    temperature = 0
    for temp in month:
        temperature += month[temp]
    ave = temperature / len(average_temp)
    print ("The average temperature in Paris is " + str(ave) + " degrees.")


def higher_temp(monthly):
    global yr_temp
    for high in monthly:
        if monthly[high] > yr_temp:
            above_average[high] = (monthly[high])
    print ("The months with above average temperatures are: " + str(above_average))

average_paris(average_temp)
higher_temp(average_temp)
