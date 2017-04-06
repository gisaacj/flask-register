from flask_script import Manager, Server,Shell
from app import app
from app import models

# Init manager object via app object
manager = Manager(app)

# Create some new commands
manager.add_command("server", Server(host='127.0.0.1', port=5000))

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=app,
                db=models.db,
                User=models.User)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
