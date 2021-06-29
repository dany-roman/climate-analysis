import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    print("Accessing homepage")
    return (
        f"Welcome to the Honolulu climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>")

# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     print("Accessing Precipitation Page")
    
#     session = Session(engine)
#     precipitation = session.query(measurement.date, measurement.prcp).all()
#     session.close()
    
#     measurements = []
#     for date, prcp in precipitation:
#         prec_dict = {}
#         prec_dict['Date'] = date
#         prec_dict['Precipitation'] = prcp
#         measurements.append(prec_dict)
  
#     return jsonify(prec_dict)

# @climate_app.route("/api/v1.0/stations")
# def stations():
#     print("Accessing Stations Page")
    
#     session = Session(engine)
#     all_stations = session.query(station.name).all()
#     session.close()
    
#     stations = []
#     for row in stations:
#         stat_dict = {}
#         stat_dict['Station'] = row
#         stations.append(stat_dict)
  
#     return jsonify(stat_dict)

# @app.route("/api/v1.0/tobs")
# def temperature():
#     print("Accessing Temperature Page")
#     return jsonify(hello_dict)

# @app.route("/api/v1.0/<start>")
# def start():
#     print("Accessing API Start Page")
#     return jsonify(hello_dict)

# @app.route("/api/v1.0/<start>/<end>")
# def range():
#     print("Accessing API Range Page")
#     return jsonify(hello_dict)

if __name__ == "__main__":
    app.run(debug=True)