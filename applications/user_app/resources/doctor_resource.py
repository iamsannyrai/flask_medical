from flask_restful import Resource

from applications.user_app.managers.user_app_manager import UserAppManager
from applications.user_app.schemas.doctor_schema import DoctorSchema


class DoctorResource(Resource):
    def __init__(self):
        self.user_app_manager = UserAppManager()
        self.doctor_schema = DoctorSchema()

    def get(self, doctor_id):
        doctor = self.user_app_manager.get_doctor_profile(doctor_id)
        self.doctor_schema.dump(doctor)
