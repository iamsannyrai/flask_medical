from core.enums import Environment


class Config:
    DEBUG = True


class DevelopmentConfig(Config):
    ENV = "development"
    pass


class ProductionConfig:
    DEBUG = False
    pass


config = {
    Environment.production: ProductionConfig,
    Environment.development: DevelopmentConfig
}
