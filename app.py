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
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        # f"/api/v1.0/<start><br/>"
        # f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    result = session.query(measurement.date, measurement.prcp).all()

    session.close()

    date_percip = []
    for date, prcp in result:
        date_percip_dict = {date:prcp}
        date_percip.append(date_percip_dict)

    # all_prcp = list(np.ravel(result))

    return jsonify(date_percip)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    result = session.query(station.station).all()

    session.close()

    all_stations = list(np.ravel(result))

    return jsonify(all_stations)

if __name__ == '__main__':
    app.run(debug=True)