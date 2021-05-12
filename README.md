# SQL_Local_Climate_Analysis

Objective: Prior to a trip to Hawaii, a climate analysis on the area is needed for better trip planning.

### Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Choice of start date and end date 

* Using SQLAlchemy `create_engine` to connect to your sqlite database.

* Using SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Query to retrieve the last 12 months of precipitation data.

* Selection of only the `date` and `prcp` values.

* Loading the query results into a Pandas DataFrame and set the index to the date column.

* Sorting the DataFrame values by `date`.

* Plotting the results using the DataFrame `plot` method.

* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designing a query to calculate the total number of stations.

* Designing a query to find the most active stations.

  * Listing the stations and observation counts in descending order.

  * Which station has the highest number of observations? Using a function such as `func.min`, `func.max`, `func.avg`, and `func.count` in queries.

* Designing a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtering by the station with the highest number of observations.

  * Plotting the results as a histogram with `bins=12`.
  * 

## Climate App

With the initial analysis, designing a Flask API based on the previous queries.

* Using Flask to create your routes.

### Routes

* `/`

  * Home page.

  * Listing all routes that are available.

* `/api/v1.0/precipitation`

  * Converting the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returning the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returning a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query of the dates and temperature observations of the most active station for the last year of data.
  
  * Returning a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returning a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


