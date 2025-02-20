from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name
    name = "Shrvan Sudhakara"  

    # System username
    user = os.getenv("USER", "codespace")

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    # Get top output
    top_output = subprocess.getoutput("top -b -n 1")

    # Format the response
    response = f"""
    <pre>
    Name: {name}
    User: {user}
    Server Time (IST): {formatted_time}

    TOP output:
    {top_output}
    </pre>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
