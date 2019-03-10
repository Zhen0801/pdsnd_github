import time
import pandas as pd
import webbrowser


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']


def go_to_Motivate():

    while True:

        web = input("All the data is provided by Motivate,\n a bike share system provider for many major cities in the United States.\n\n Enter 'go' to explore the Motivate web or enter 'continue' to continue explore the data here.\n")
        if web.lower() == 'go' or web.lower() == 'g':
            webbrowser.open('https://www.motivateco.com')
            break
        elif web.lower() == 'continue' or web.lower() == 'c':
            print('Maybe next time.')
            break
        else:
            print('Invalid input. Please try again:\n')






def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHey! Let\'s explore some US bikeshare data! Exciting !')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input('There are three cities : chicago, new york city and washington, which city would you like to explore?\n').lower()
            # TO DO: get user input for month (all, january, february, ... , june)
            month = input('which month(s) would u like to explore? jan, feb, mar, apr, may, jun or all ?\n').lower()
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('which day(s) would u like to explore? monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n').lower()
            print('\nSo, you want to explore {}\'s US bikeshare data. Filter(s) are ->  month : {} ; day of the week: {} '.format(city, month, day))

            df = load_data(city, month, day)

        except Exception as error:
            print('\nexception occurred :{}, please try again :) \n'.format(error))
            continue

        answer = input('\nWould you like to reselect to ciy or time? Enter yes or no.\n')
        if answer.lower() == 'no' or answer.lower() == 'n':
            break

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int

        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # df.interpolate(method = 'linear', axis = 0)

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    month_loc = df['month'].mode()[0]
    common_month = months[month_loc - 1]


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('The most common month is {}.\nThe most common day of the week is {}.\nThe most common hour of the day is {}.\n '.format(common_month, common_day, common_hour))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]


    #TO DO: display most frequent combination of start station and end station trip

    new_df = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('The most commonly used start station is {}.\nThe most commonly used end station is {}.\nThe most frequent combination of start station and end station trip is \n{}'.format(start_station, end_station, new_df.head(1)))




def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_sec = df['Trip Duration'].sum()
    total_min = total_sec/60

    # TO DO: display mean travel time

    mean_sec = df['Trip Duration'].mean()
    mean_min = mean_sec/60


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('The total travel time is {}min.\nThe mean travel time is {}min.'.format(total_min, mean_min))


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    df.dropna(axis=0)
    # TO DO: Display counts of different user types
    user_type = df.groupby(['User Type']).size()

    # TO DO: Display counts of gender
    if 'Gender' in df:
        counts_gender = df.groupby(['Gender']).size()

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        most_recent =  df['Birth Year'].max()
        most_common =  df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    if 'Gender' and 'Birth Year'in df:
        print('{}\n{}\nThe earliest year of birth is {}.\nThe most recent year of birth is {}.\nThe most common year of birth is {}.\n '.format(user_type, counts_gender, earliest, most_recent, most_common))
    else:
        print('{}\n'.format(user_type))


def original_data(df):

    answer = input('\n Would you like to view some raw BikeShare data ? Enter yes or no. Data will be displayed in five rows at a time.\n')
    print(answer)
    if answer.lower() == 'yes' or answer.lower() == 'y':
        print(len(df))
        print(df.head())
        start = 6
        while True:
            a = input("Want to explore further? We still have {} rows of raw data. Enter 'yes' to see another five rows or 'no' to stop.\n".format(len(df)-start+1))
            if a.lower() == 'yes' or a.lower() == 'y':
                print(df.iloc[start:start+5])
                start += 5
            else:
                break



def main():
    while True:
        go_to_Motivate()
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        original_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks for exploring our data! Hope to see you next time! Have a nice day! ')
            break


if __name__ == "__main__":
	main()
