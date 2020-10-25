
# Imports
import os
from api import flask_app

# Create the port
port = int(os.environ.get("PORT", 5000))


# Run the app
if __name__ == '__main__':
    flask_app.run('0.0.0.0', port=port, debug=False, threaded=False)
