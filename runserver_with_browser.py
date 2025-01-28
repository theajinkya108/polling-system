import subprocess
import webbrowser
import time

# Start the Django server in the background
subprocess.Popen(["py", "manage.py", "runserver"])

# Wait a moment to ensure the server starts
time.sleep(2)

# Open the browser
webbrowser.open("http://127.0.0.1:8000/")
