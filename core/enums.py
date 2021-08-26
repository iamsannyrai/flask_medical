from enum import Enum


# represents environment in which the app runs
class Environment(Enum):
    production = "production"
    development = "development"
