## udacity-bikeshare
udacity-bikeshare creates an **interactive experience** in the terminal. It takes in raw input to answers questions about data related to **bike share systems** for three major cities in the United States—_Chicago_, _New York City_, and _Washington_.


## Date created
- README file: Mar-08-2019

- Project: Feb-25-2019

## Install
To run this project, you need:

- A terminal application (Terminal on Mac and Linux or Cygwin on Windows)

- Install [Python 3](https://www.python.org/downloads/) and [Anaconda](https://www.anaconda.com/distribution/)
- Install pandas using Anaconda

    `$ conda install pandas=0.22`

- Run bikeshare.py

     `$ python bikeshare.py`



## Information you can get from system

#### 1 Popular times of travel  
* most common month
* most common day of week
* most common hour of day

#### 2 Popular stations and trip
* most common start station
* most common end station
* most common trip from start to end

#### 3 Trip duration
* total travel time
* average travel time

#### 4 User info
* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

#### 5 View original data from  three city's dataset files


## The Datasets

The datasets for the first six months of 2017 is Randomly selected by [**Udacity**](https://eu.udacity.com).

All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

## Files used

Three city dataset files:

- chicago.csv

- new_york_city.csv

- washington.csv

The **original** datasets files can be accessed here if you'd like to see them: [Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data).

_*All the data is provided by [Motivate](https://www.motivateco.com), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns._

## Credits
The data files and programming instructions are provided by Udactiy's [Programming for Data Science Nanodegree Program]. :bowtie:
