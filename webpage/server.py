import socket

from flask import *


# ARDUINO CONFIGURATION
# Set ARDUINO_MDNS_NAME to the MDNS name of the Arduino (by default arduino.local),
# and keep ARDUINO_IP equal to None to have the server attempt to resolve the Arduino
# IP address automatically.  If this resolution fails, you can set the ARDUINO_IP value
# manually below to the IP (as a string, for example '192.168.1.100') to skip the MDNS
# lookup.  
# - On Windows you need Bonjour installed to resolve MDNS names.  You can install it from
#   here with the Bonjour Print Services for Windows download: http://support.apple.com/kb/DL999
# - On Linux Bonjour support is likely installed already (if you use Ubuntu for example).
#   If not, install Avahi: http://avahi.org/
# - On Mac OSX Bonjour is installed automatically.
ARDUINO_MDNS_NAME = 'arduino.local'
ARDUINO_IP = None

# Flask app configuration
DEBUG = True

# Query the IP address of the arduino.
if ARDUINO_IP is None:
	try:
		ARDUINO_IP = socket.gethostbyname(ARDUINO_MDNS_NAME)
	except socket.gaierror:
		raise RuntimeError('Could not find Arduino at address %s! Set ARDUINO_IP manually to the IP address of the Arduino and run again.' % ARDUINO_MDNS_NAME)

print 'Found Arduino at IP', ARDUINO_IP

# Create a simple model to be used in page templates.
model = { 'arduino_ip': ARDUINO_IP }

# Initialize flask app.
app = Flask(__name__)
app.config.from_object(__name__)

# Main view for rendering the web page.
@app.route('/')
def index():
	return render_template('index.html', model=model)

# Start running the flask app, by default on port 5000.
if __name__ == '__main__':
	app.run(host='0.0.0.0')
