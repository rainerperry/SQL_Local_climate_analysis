import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask Setup

app = Flask(__name__)


# Flask Routes


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
   )


@app.route("/api/v1.0/precipitation")


def precipitation():

    session = Session(engine)

    prec_data = session.query(Measurement.prcp, Measurement.date).filter(Measurement.date > '2016-08-23').all()

    session.close()

    prec_list = list(np.ravel(prec_data))

    return jsonify(prec_list)


@app.route("/api/v1.0/stations")
def stations():

    #Create session link from Python to hawaii database for a list of stations
    session = Session(engine)

    results = session.query(Station.station).all()

    session.close()

    #convert query results into list
    station_list = list(np.ravel(results))

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():

    #Query the dates and temperature observations of the most active station for the last year of data.
    session = Session(engine)

    top_station_tobs = session.query(Measurement.tobs, Measurement.date). \
        filter(Measurement.station == 'USC00519281').filter(Measurement.date > '2016-08-23').all()

    session.close()

    #Create a dictionary from the query data for the Json list
    top_station_tobs_list = []

    for date, tobs in top_station_tobs:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        top_station_tobs_list.append(tobs_dict)

    return jsonify(top_station_tobs_list)


@app.route("/api/v1.0/<start>")
def start(start):

    session = Session(engine)


    temperatures = session.query(Measurement.station, func.min(Measurement.tobs),
        func.avg(Measurement.tobs), func.max(Measurement.tobs)). \
        filter(Measurement.date == start).all()

    session.close()

    return jsonify(temperatures)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):

    session = Session(engine)

    temps_two = session.query(Measurement.station, func.min(Measurement.tobs),
            func.avg(Measurement.tobs), func.max(Measurement.tobs)). \
            filter(Measurement.date > start).filter(Measurement.date < end).all()

    session.close()

    return jsonify(temps_two)


if __name__ == '__main__':
    app.run(debug=True)