import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

#designate path names
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h3>Available Routes</h3>"
        f"<ul><li>/api/v1.0/precipitation</li>"
        f"<li>/api/v1.0/stations</li>"
        f"<li>/api/v1.0/tobs</li>"
        f"<li>/api/v1.0/start</li>"
        f"<li>/api/v1.0/start/end</li>"
    )

# show date and precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    result = session.query(measurement.date, measurement.prcp).all()

    session.close()

    date_percip = []
    for date, prcp in result:
        date_percip_dict = {date:prcp}
        date_percip.append(date_percip_dict)

    return jsonify(date_percip)

#show the list of sations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    result = session.query(station.station, station.name).all()

    session.close()

    all_stations = list(np.ravel(result))

    return jsonify(all_stations)

#show temperature observations after for 1 year to date after the last observation
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    rct_date = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]

    year_to_date = dt.datetime.strptime(rct_date,'%Y-%m-%d') - dt.timedelta(days=365)

    most_active = session.query(measurement.station, func.count(measurement.station)).\
    group_by(measurement.station).\
    order_by(func.count(measurement.station).desc()).first()[0]

    result = session.query(measurement.date,measurement.tobs).\
        filter(measurement.date >= year_to_date).\
        filter(measurement.station == most_active).all()


    session.close()

    return jsonify(result)

#show min, avg, and max tobs between specified dates
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_date(start, end = '2017-08-07'):
    
    session = Session(engine)

    result = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter((measurement.date >= start) & (measurement.date <= end)).all()[0]
    res = {f'{start} - {end}': result}

    return res

if __name__ == "__main__":
    app.run(debug=True)