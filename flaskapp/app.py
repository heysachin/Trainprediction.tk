
# Created by Sachin Dev on 09/06/18

import csv
from flask import Flask, render_template, request
from common.database import Database
from models.stations.station import Station
from models.timetables.timetable import TimeTable
from models.trains.train import Train

app = Flask(__name__)
app.secret_key = 'sachin'


@app.before_first_request
def _init_db():
    Database.initialize()


@app.route('/trains/btw', methods=['POST'])
def trains_between_stations():
    source = request.form['source']
    source = source.upper()
    destination = request.form['destination']
    destination = destination.upper()
    trains = TimeTable.trains_btw_stations(source, destination)
    return render_template("trains_btw_stations.html", trains=trains, source=source,destination=destination)


@app.route('/timetable/<string:train_no>')
def get_timetable(train_no):
    train_class = Train.get_by_id(train_no)
    stations = TimeTable.get_stations_by_train(train_no)
    return render_template("timetable.html", stations=stations, train_class=train_class)


@app.route('/')
def home():
    stations = Station.all()
    return render_template('home.html', stations=stations)

if __name__ == "__main__":
    app.debug=True
    app.run(host='127.0.0.1')
