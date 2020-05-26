
from flask import Flask, request, json
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

secretKey = "21@Century" #os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="cse17",
    password=secretKey,
    hostname="cse17.mysql.pythonanywhere-services.com",
    databasename="cse17$default",
)

app = Flask(__name__)
app.config["DEBUG"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = secretKey
app_root = "/api/v1"

db = SQLAlchemy(app)

class Donor(db.Model):
    __tablename__ = "Donor"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255))
    bloodType = db.Column(db.String(10))
    birthDate = db.Column(db.DateTime)
    phoneNumber = db.Column(db.String(255))

Donates = db.Table('Donates',
    db.Column('donorId', db.Integer, db.ForeignKey('Donor.id')),
    db.Column('donationId', db.Integer, db.ForeignKey('Donation.id'))
)

class Donation(db.Model):
    __tablename__ = "Donation"
    id = db.Column(db.BigInteger, primary_key=True)
    donationDate = db.Column(db.DateTime)
    location = db.Column(db.String(255))
    notes = db.Column(db.String(1000))
    donors = db.relationship('Donor', secondary=Donates, backref='donations')

@app.route(app_root + '/donors/<id>', methods=['GET'])
def getDonor(id):
	donor = db.session.query(Donor).filter(Donor.id==id).first();
	if donor is not None:
		return json.dumps(donor.__dict__, indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donors', methods=['GET'])
def getDonors():
	donors = db.session.query(Donor).all();
	if(donors is not None):
		return json.dumps([d.__dict__ for d in donors], indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donors', methods=['POST'])
def createDonors():
	donor_request = request.get_json()
	donor = Donor.query.filter(Donor.id==donor_request["id"]).first()
	if donor is not None:
		donor.name = donor_request['name']
		donor.bloodType = donor_request['bloodType']
		donor.birthDate = datetime.strptime(donor_request['birthDate'], '%Y-%m-%d')
		donor.phoneNumber = donor_request['phoneNumber']
		db.session.commit()
		return('',200)
	else:
		donor = Donor(name=donor_request['name'],bloodType=donor_request['bloodType'],
			birthDate=datetime.strptime(donor_request['birthDate'], '%Y-%m-%d'),
			phoneNumber=donor_request['phoneNumber'])
		db.session.add(donor)
		db.session.commit()
		return('',201)

@app.route(app_root + '/donations/<id>', methods=['GET'])
def getDonation(id):
	donation = db.session.query(Donation).filter(Donation.id==id).first();
	if donation is not None:
		return json.dumps(donation.__dict__, indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donations/<id>/donors', methods=['GET'])
def getDonationDonors(id):
	donation = db.session.query(Donation).filter(Donation.id==id).first();
	if donation is not None and donation.donors is not None:
		return json.dumps([d.__dict__ for d in donation.donors], indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donations', methods=['GET'])
def getDonations():
	donations = db.session.query(Donation).order_by(-Donation.donationDate).all()
	if(donations is not None):
		return json.dumps([d.__dict__ for d in donations], indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donations', methods=['POST'])
def createDonation():
    donation_request = request.get_json()
    donation = Donation.query.filter(Donation.id==donation_request["id"]).first()
    if donation is not None:
    	donation.donationDate = datetime.strptime(donation_request['donationDate'], '%Y-%m-%d')
    	donation.location = donation_request['hospital']
    	donation.notes = donation_request['notes']
    	donorIds=donation_request['donorIds']
    	donors = []
    	for id in donorIds:
    		donor = Donor.query.filter(Donor.id==id).first()
    		if donor is not None:
    		   donors.append(donor)
    	donation.donors = donors
    	db.session.commit()
    	return('',200)
    else:
        donation = Donation(donationDate=datetime.strptime(donation_request['donationDate'], '%Y-%m-%d'),
        	location=donation_request['location'], notes=donation_request['notes'])

        donorIds=donation_request['donorIds']
        for id in donorIds:
        	#print(id)
        	donor = Donor.query.filter(Donor.id==id).first()
        	if donor is not None:
        		donation.donors.append(donor)
        db.session.add(donation)
        db.session.commit()
        return('',201)
