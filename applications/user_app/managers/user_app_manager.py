from applications.user_app.models.doctor_model import DoctorModel
from applications.user_app.models.patient_model import PatientModel


class UserAppManager:
    def get_doctor_profile(self, doctor_id):
        profile = DoctorModel.query.get(doctor_id)
        return profile

    def get_patient_profile(self, patient_id):
        profile = PatientModel.query.get(patient_id)
        return profile
