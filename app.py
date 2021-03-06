import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h3>Available Routes</h3>"
        f"<ul><li>/api/v1.0/precipitation</li>"
        f"<li>/api/v1.0/stations</li>"
        f"<li>/api/v1.0/tobs</li>"
        +"<li>/api/v1.0/<{start date}><li>" +
        "/api/v1.0/{<start date}/{end date}></li></ul>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    result = session.query(measurement.date, measurement.prcp).all()

    session.close()

    # date_percip = [{"Date": result[0], "precipitation": result[1]} for date, prcp in result]

    date_percip = []
    for date, prcp in result:
        date_percip_dict = {date:prcp}
        date_percip.append(date_percip_dict)

    return jsonify(date_percip)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    result = session.query(station.station, station.name).all()

    session.close()

    all_stations = list(np.ravel(result))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    # result = session.query(measurement.station).\
    # group_by(measurement.station).\
    # order_by(func.count(measurement.station).desc()).first()

    return {date: tobs for date, tobs in session.query(measurement.date, measurement.tobs).all()}

    session.close()

    return jsonify(result)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start><end>")
def start_end(start, end):





if __name__ == '__main__':
    app.run(debug=True)
    session = Session(engine)

        # geronimo's code in percipitation

    # response = {}
    # for date, prcp in result:
    #     responde [date]: prcp

    # print(response)