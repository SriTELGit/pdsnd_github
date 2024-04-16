>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
Created 2024, April 16.

### Project Title
Bikeshare data analysis

### Description
This project develops the code to read .csv files containing information/data about bike sharing in 3 cities in USA (Chicago, NewYork & Washington).
The data has comma sperated values in rows, having the following columns - 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year'. We use Pandas dataframe functionality to create few new columns ( 'hour', 'Start_End_Combo', 'day_of_week' ) and showcase information ( using sum(), mean(), mode() functionalities of Pandas dataframe ).

bikeshare_2.py has following functions 

get_filters() - Asks user to specify a city, month, and day to analyze.
load_data(city, month, day) -  Loads data for the specified city and filters by month and day if applicable.

time_stats(df) - Displays statistics on the most frequent times of travel - most common month, most common day of week, most comman hour
station_stats(df) - Displays statistics on the most popular stations - most used start station, most used end station
trip_duration_stats(df) - Displays statistics on the total and average trip duration.

user_stats(df) - Displays statistics on bikeshare user, their Gender, UserType, and year of birth

display_data(df) - Displays 5 rows of data, of the process Pandas data frame, at a time


### Files used
Data .csv files are not checked in.
Python code, bikeshare_2.py is checked in.


### Credits
This is from Udacity course.

