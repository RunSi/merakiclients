import sys
activate_this = '/home/ubuntu/Python3code/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0, "/var/www/meraki")
from meraki import app as application
