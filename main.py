
# Imports
import os

port = int(os.environ.get("PORT", 5000))
api = create_app()


# Run the app
if __name__ == '__main__':
    api.run('0.0.0.0', port=port, debug=False, threaded=True)
