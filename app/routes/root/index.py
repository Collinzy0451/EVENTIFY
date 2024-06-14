from app import app

@app.route('/')
def home():
    return "Hello Collinzy. wetin dey sup?"