'''
Created on Nov 17, 2020
Random Date Generator
Narration: This code allows the user to select 2 years, and find a random date between those two years. The user can also choose the same year to find a date in only a specific year. The random date is the printed
Features: Random Date Generation, Year Selection, TTS, Printed Calendar, Loop and try/except for no errors, day of the week with calendar function
Log 1.0 Initial Version
Log 1.1 Added input for year chosen
Log 1.2 Fixed bug with negative numbers, Fixed bug with inputted strings
Log 1.3 Added day of the week
Log 1.4 Added TTS for the output, changed rate of speaker and gender
Log 1.5 Added while loop so if an error is found, the user can try again without having to run the code again. Fixed bug with having the ending year higher than the starting, Fixed bug with space in inputs. Fixed bug with Tuesdays not being displayed properly
Bugs: None
@author: apauley24
'''

#Sets up functions for TTS and calendar by importing them
import random
import calendar
import pyttsx3
from calendar import weekday
from calendar import prmonth

def main():
    
    #Sets up loop for errors
    
    loop_check = True
    while loop_check == True:
        
        #Title
        
        print("Random Date Generator")
        
        #Sets up tts voice and the rate and gender
        
        month_tts = pyttsx3.init()
        rate = month_tts.getProperty('rate')
        month_tts.setProperty('rate', 100)
        voices = month_tts.getProperty('voices')
        month_tts.setProperty('voice', voices[1].id) 
        
        #Asks user for input
        
        year_start = input("Enter starting year")
        year_end = input("Enter ending year")
        
        #Sets up try for code to catch errors
        
        try:
            
            #Converts the two year variables into spaceless integers
            
            year_start = year_start.strip()
            year_end = year_end.strip()
            year_end = int(year_end)
            year_start = int(year_start)  
            
            #Catches if the user inputs negative numbers so the code doesn't break.
            
            if year_end < 0 or year_start < 0:
                print("No Negative Numbers")
                
            #If everything works, runs the code
            
            else:
                
                #Finds the year 
                
                year = random.randint(year_start, year_end)
                
                #Stop loop so it doesn't repeat because there was no errors
                
                loop_check = False
                
                #Chooses a random month
                
                month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                month_choice = random.choice(month)
                
                #If else for converting the month to a number 1-12
                
                if month_choice == "January":
                    month_num = 1
                elif month_choice == "February":
                    month_num = 2
                elif month_choice =="March":
                    month_num = 3
                elif month_choice =="April":
                    month_num = 4
                elif month_choice =="May":
                    month_num = 5
                elif month_choice =="June":
                    month_num = 6
                elif month_choice =="July":
                    month_num = 7
                elif month_choice =="August":
                    month_num = 8
                elif month_choice =="September":
                    month_num = 9
                elif month_choice =="October":
                    month_num = 10
                elif month_choice == "November":
                    month_num = 11
                elif month_choice =="December":
                    month_num = 12
                    
                #If else to see how many days in month. Checks for leap years and if it has 30 or 31 days
                
                if year % 4 == 0 and month_choice == "February":
                    
                    #Chooses a random day depending on month
                    
                    day = random.randint(1,29)
                    
                    #Finds the weekday of he date selected
                    
                    week_day = calendar.weekday(year, month_num, day)
                    
                    #Converts weekday number to a string
                    
                    if week_day == 0:
                        week_day = "Monday"
                    elif week_day == 1:
                        week_day = "Tuesday"
                    elif week_day == 2:
                        week_day = "Wednesday"
                    elif week_day == 3:
                        week_day = "Thursday"
                    elif week_day == 4:
                        week_day = "Friday"
                    elif week_day == 5:
                        week_day = "Saturday"
                    elif week_day == 6:
                        week_day = "Sunday"
                        
                    #Prints answer
                    
                    print("Your Random Day is:", week_day, month_choice, day, year)
                    
                    #Says the answer in tts
                    
                    month_tts = pyttsx3.init()
                    month_tts.say("Your Random Day is:"+ str(week_day) + str(month_choice) + str(day) +  str(year))
                    month_tts.runAndWait()
                    
                    #Prints a text calender of the month
                    
                    prmonth(year, month_num, w=1, l=1)
                    
                elif year % 4 != 0 and month_choice == "February":
                    
                    day = random.randint(1,28)
                    
                    week_day = calendar.weekday(year, month_num, day)
                    
                    if week_day == 0:
                        week_day = "Monday"
                    elif week_day == 1:
                        week_day = "Tuesday"
                    elif week_day == 2:
                        week_day = "Wednesday"
                    elif week_day == 3:
                        week_day = "Thursday"
                    elif week_day == 4:
                        week_day = "Friday"
                    elif week_day == 5:
                        week_day = "Saturday"
                    elif week_day == 6:
                        week_day = "Sunday"
                        
                    print("Your Random Day is:", week_day, month_choice, day, year)
                    
                    month_tts = pyttsx3.init()
                    month_tts.say("Your Random Day is:"+ str(week_day) + str(month_choice) + str(day) +  str(year))
                    month_tts.runAndWait()
                    
                    prmonth(year, month_num, w=1, l=1)
                    
                elif month_choice == "September" or month_choice == "April" or month_choice == "June" or month_choice == "November":
                    
                    day = random.randint(1,30)
                    
                    week_day = calendar.weekday(year, month_num, day)
                    
                    if week_day == 0:
                        week_day = "Monday"
                    elif week_day == 1:
                        week_day = "Tuesday"
                    elif week_day == 2:
                        week_day = "Wednesday"
                    elif week_day == 3:
                        week_day = "Thursday"
                    elif week_day == 4:
                        week_day = "Friday"
                    elif week_day == 5:
                        week_day = "Saturday"
                    elif week_day == 6:
                        week_day = "Sunday"
                        
                    print("Your Random Day is:", week_day, month_choice, day, year)
                    
                    month_tts = pyttsx3.init()
                    month_tts.say("Your Random Day is:"+ str(week_day) + str(month_choice) + str(day) +  str(year))
                    month_tts.runAndWait()
                    
                    prmonth(year, month_num, w=1, l=1)
                else:
                    
                    day = random.randint(1,31)
                    
                    week_day = calendar.weekday(year, month_num, day)
                    
                    if week_day == 0:
                        week_day = "Monday"
                    elif week_day == 1:
                        week_day = "Tuesday"
                    elif week_day == 2:
                        week_day = "Wednesday"
                    elif week_day == 3:
                        week_day = "Thursday"
                    elif week_day == 4:
                        week_day = "Friday"
                    elif week_day == 5:
                        week_day = "Saturday"
                    elif week_day == 6:
                        week_day = "Sunday"
                        
                    print("Your Random Day is:", week_day, month_choice, day, year)
                    
                    month_tts = pyttsx3.init()
                    month_tts.say("Your Random Day is:"+ str(week_day) + str(month_choice) + str(day)  +  str(year))
                    month_tts.runAndWait()
                    
                    prmonth(year, month_num, w=1, l=1)
        
        #if there is an error, catches it with except and runs the code again
                   
        except:
            
            #Sees if the answer is because the ending year is less than the starting year, tells user what to do
            
            if year_end < year_start:
                print("The starting year has to be less than the ending year.")
            
            #Prints general error message
                
            print("Please only input whole numbers")
    
       
    
    
    
    
    
    
if __name__ == "__main__":
    main()