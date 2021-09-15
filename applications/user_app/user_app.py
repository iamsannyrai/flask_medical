from flask import Blueprint
from flask_restful import Api

from applications.user_app.resources.doctor_resource import DoctorResource
from applications.user_app.resources.patient_resource import PatientResource

user_app = Blueprint('user_app', __name__)
api = Api(user_app)

api.add_resource(DoctorResource, "/doctors", "/doctors/<role_id>")
api.add_resource(PatientResource, "/patients", "/patients/<role_id>")