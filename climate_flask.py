# Dependencies
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Access sqlite file and reflect
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Declare measurement and station tables
measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    print("Accessing homepage")
    return (
        f"<br/>Welcome to the Honolulu Climate API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/startdate | Note: Enter date as 'Year-Mo-Da'<br/>"
        f"/api/v1.0/startdate/enddate | Note: Enter date as 'Year-Mo-Da'<br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Accessing Precipitation Page")
    
    # query for date and precipitation
    session = Session(engine)
    precipitation = session.query(measurement.date, measurement.prcp).all()
    session.close()
    
    # create a dictionary of the precipitation data
    measurements = []
    for date, prcp in precipitation:
        prec_dict = {}
        prec_dict['Date'] = date
        prec_dict['Precipitation'] = prcp
        measurements.append(prec_dict)
    
    # convert to JSON
    return jsonify(measurements)

@app.route("/api/v1.0/stations")
def stations():
    print("Accessing Stations Page")
    
    #query for station id and name
    session = Session(engine)
    all_stations = session.query(station.id, station.name).all()
    session.close()
    
    # create a dictionary of station names
    all_station_names = []
    for station_id, name in all_stations:
        stat_dict = {}
        stat_dict['Station ID'] = station_id
        stat_dict['Station'] = name
        all_station_names.append(stat_dict)
  
    # convert to JSON
    return jsonify(all_station_names)

@app.route("/api/v1.0/tobs")
def temps():
    print("Accessing Temperature Observations Page")
    
    # query for temperature measurements during the final 12 months
    session = Session(engine)
    session.query(measurement.date).order_by(measurement.date.desc()).first()
    last_date = dt.date(2017, 8, 31)
    one_year_ago = last_date - dt.timedelta(days=365)
    q_prec = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date <= last_date).\
        filter(measurement.date >= one_year_ago).\
        order_by(measurement.date.asc()).all()
    session.close()
    
    # create a dictionary of filtered data
    all_tobs = []
    for date, prcp in q_prec:
        tobs_dict = {}
        tobs_dict['Date'] = date
        tobs_dict['Precipitation'] = prcp
        all_tobs.append(tobs_dict)
  
    # convert to JSON
    return jsonify(all_tobs)

@app.route(f"/api/v1.0/<start_date>")
def temp_stat_start(start_date):
    print("Accessing Temperature Statistics (Start Date) Page")
    
    # query for measurements after the start date
    session = Session(engine)
    temp_measure = session.query(measurement.tobs)\
        .filter(measurement.date >= start_date)\
        .order_by(measurement.tobs.desc()).all()
    session.close()
    
    # create a list from tuples
    all_temps = []
    for temp in temp_measure:
        all_temps.append(temp[0])

    # calculate stats
    TMIN = min(all_temps)
    TMAX = max(all_temps)
    TAVG = round((sum(all_temps)/len(all_temps)), 1)

    # create a dictionary of stats
    temp_stats = {
        'TMIN': TMIN,
        'TMAX': TMAX,
        'TAVG': TAVG
    }

    # convert to JSON
    return jsonify(temp_stats)

@app.route(f"/api/v1.0/<start_date>/<end_date>")
def temp_stat_range(start_date, end_date):
    print("Accessing Temperature Statistics (Date Range) Page")
    
    # query for temp measurements between two dates
    session = Session(engine)
    temp_measure = session.query(measurement.tobs)\
        .filter(measurement.date >= start_date)\
        .filter(measurement.date <= end_date)\
        .order_by(measurement.tobs.desc()).all()
    session.close()
    
    # create a list of measurements
    all_temps = []
    for temp in temp_measure:
        all_temps.append(temp[0])

    # calculate stats
    TMIN = min(all_temps)
    TMAX = max(all_temps)
    TAVG = round((sum(all_temps)/len(all_temps)), 1)

    # create a dictionary of stats
    temp_stats = {
        'TMIN': TMIN,
        'TMAX': TMAX,
        'TAVG': TAVG
    }

    # convert to JSON
    return jsonify(temp_stats)

if __name__ == "__main__":
    app.run(debug=True)