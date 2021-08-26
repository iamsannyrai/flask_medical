from core.enums import Environment
from init import create_app

app = create_app(Environment.development)

if __name__ == '__main__':
    app.run()
