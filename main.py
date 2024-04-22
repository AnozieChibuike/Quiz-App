from app import app, db

from app.models.user import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db,'Users':User}
