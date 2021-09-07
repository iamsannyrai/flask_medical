from core.extensions import ma


class RoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "role")
