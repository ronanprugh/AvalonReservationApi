from flask import Flask
from flask import request
from service.Reservation import Reservation

app = Flask(__name__)

@app.route("/reservation", methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        return Reservation.postReservation(request.form)
    elif request.method == 'GET':
        return Reservation.getReservation()



