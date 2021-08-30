import os
from dotenv import load_dotenv
from core.enums import Environment

load_dotenv()


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    pass


class ProductionConfig:
    DEBUG = False
    pass


config = {
    Environment.production: ProductionConfig,
    Environment.development: DevelopmentConfig
}
