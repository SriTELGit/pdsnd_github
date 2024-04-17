import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LST = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_OF_WEEK_LST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    selC = None
    city = ''
    while selC == None:
        city = input('Enter city whose data to analyse chicago/newyork/washington: ')
        city = city.lower()
        selC = CITY_DATA.get(city)
        if(selC == None):
            print('have to select one of 3 cities')

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month not in MONTH_LST:
        month = input('Enter month between january to june or "all" for all months: ')
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in DAY_OF_WEEK_LST:
        day = input('Enter weekday between monday to sunday or "all" for all days: ')
        day = day.lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['Start_End_Combo'] = df['Start Station']+' - '+df['End Station']
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    #print(df.head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nmost common month: ', df['month'].mode()[0])


    # display the most common day of week
    print('\nmost common day of week: ', df['day_of_week'].mode()[0])


    # display the most common start hour
    print('\nmost common start hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nmost used start station: ', df['Start Station'].mode()[0])


    # display most commonly used end station
    print('\nmost used end station: ', df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    print('\nmost used start - end station combo: ', df['Start_End_Combo'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\ntotal travel time: ', df['Trip Duration'].sum())


    # display mean travel time
    print('\nmean travel time: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df['User Type'].value_counts()

    # Display counts of gender
    if 'Gender' in df.columns:
        df['Gender'].value_counts()


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nmost earlies, recent and most comman birth year: ', df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0] )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data at a time."""

    showD = True
    start_loc = 0
    while ( (showD == True) and (start_loc < df.shape[0]) ):
        ansyn = input('Do you want to see next 3 rows of data? (yes/no): ')
        ansyn = ansyn.lower()
        if(ansyn == 'yes'):
            print(df.iloc[start_loc:(start_loc+3)])
            showD = True
            start_loc += 3
        else:
            showD = False
            

def restartOrNot():
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    return restart

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restrt = restartOrNot()
        if restrt.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
