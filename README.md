# SQLAlchemy 

![surfs-up.png](Images/surfs-up.png)

This project analyzes data contrived from weather stations all around Honolulu, Hawaii and is used to determine the best time of year (if any) to plan a vacation to the island.

## Step 1 - Climate Analysis and Exploration

Using Python and SQLAlchemy a basic climate analysis and data exploration of the climate database is conducted. All of the following analysis is completed by using SQLAlchemy ORM queries, Pandas, and Matplotlib.

The folowing steps show the process and tools used for the initial set up.

* SQLAlchemy - `create_engine` to connect to the sqlite database.

* SQLAlchemy - `automap_base()` to reflect the tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Python - Link to the database by creating an SQLAlchemy session.


### Precipitation Analysis

* First, the most recent date in the data set is identified.

* Using this date, the last 12 months of precipitation data is retrieved by querying the 12 preceding months of data.

* Only the `date` and `prcp` values are selected.

* The query results are then loaded into a Pandas DataFrame and the index is set to the date column.

* The DataFrame is sorted by `date`.

* The results are plotted using the DataFrame `plot` method.

  ![precipitation](Images/precipitation.png)

* Using Pandas, the summary statistics for the precipitation data are printed.

### Station Analysis

* A query is designed to calculate the total number of stations in the dataset.

* A query is designed to find the most active stations (i.e. which stations have the most rows?).

  * The stations and observation counts are listed in descending order.

  * Using the most active station id, the lowest, highest, and average temperature is calculated.

* A query is designed to retrieve the last 12 months of temperature observation data (TOBS).

  * The dataset is filtered by the station with the highest number of observations.

  * The last 12 months of temperature observation data for this station is queried.

  * A histogram plots the results with `bins=12`.

    ![station-histogram](Images/station-histogram.png)


- - -

## Step 2 - Climate App

Now that the initial analysis is complete, a Flask API is designed based on the queries that were just developed.


### Routes

* `/`

  * Home page.

  * List of all routes that are available.

* `/api/v1.0/precipitation`

  * The query results are converted to a dictionary using `date` as the key and `prcp` as the value.

  * This returns the JSON representation of the dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

  * The dates and temperature observations of the most active station for the last year of data are queried.

  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date are calculated.

  * When given the start and the end date, `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive are calculated.

## Additional Content

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Using pandas to perform this portion.

  * The date column format is converted from string to datetime.

  * The date column is set as the DataFrame index

  * The date column is dropped

* The average temperature in June at all stations across all available years in the dataset is identified as well as temperature.

* A t-test determines whether the difference in the means, if any, is statistically significant.

### Temperature Analysis II

* Looking to take a trip from August first to August seventh of this year. Using historical data in the dataset, the temperature from the previous year is found to determine whether conditions might or might not be ideal.

* The notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Using the `calc_temps` function, the min, avg, and max temperatures for the trip are calculated using the matching dates from a previous year.

* The min, avg, and max temperature from your previous query is plotted as a bar chart.

    ![temperature](Images/temperature.png)
