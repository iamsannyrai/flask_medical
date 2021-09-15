from core.extensions import ma


class DoctorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
            "id", "full_name", "dob", "gender", "age", "email", "phone_number", "blood_group", "password", "role_id",
            "role", "nmc_number")
