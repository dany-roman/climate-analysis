# Climate Analysis



### **Objective**

Use SQLAlchemy, Pandas, FLASK API, and Matplotlib to analyze temperature and precipitation data from Honolulu, HI.



### Development

#### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.
* Load the query results into a Pandas DataFrame
* Plotted the results using Matplotlib
* Created a summary of precipitation data statistics



#### Station Analysis

* Designed a query to calculate the total number of stations.
* Designed a query to find the most active stations.

* Designed a query to retrieve the last 12 months of temperature observations from the most active station.
* Plotted the results as a histogram.



#### Climate App

* Created an app using Flask API to show precipitation, station, and temperature data in Honolulu, HI
* Available routes:
  * /api/v1.0/precipitation
  * /api/v1.0/stations
  * /api/v1.0/tobs
  * /api/v1.0/<start>
  * /api/v1.0/<start>/<end>

