#!/usr/bin/env python3
"""
WSGI entry point for production deployment
"""

import os
import sys

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from simple_pos import app, socketio

if __name__ == "__main__":
    # For production deployment with gunicorn
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
else:
    # For WSGI servers
    application = app
