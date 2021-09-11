from flask_restful import Resource

from applications.user_app.managers.user_app_manager import UserAppManager
from applications.user_app.schemas.patient_schema import PatientSchema


class PatientResource(Resource):
    def __init__(self):
        self.user_app_manager = UserAppManager()
        self.patient_schema = PatientSchema()

    def get(self, patient_id):
        patient = self.user_app_manager.get_patient_profile(patient_id)
        self.patient_schema.dump(patient)
