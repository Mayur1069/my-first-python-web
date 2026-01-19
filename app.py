from flask import Flask

# Create the app instance
app = Flask(__name__)

# Define what happens when someone visits the main page "/"
@app.route("/")
def hello_world():
    return """
    <html>
        <body style="background-color: #f0f0f0; text-align: center; font-family: sans-serif; padding-top: 50px;">
            <h1 style="color: #2c3e50;">Success! My Website is Live.</h1>
            <p>This page is being served by <strong>Python</strong> and <strong>Flask</strong>.</p>
            <div style="font-size: 50px;">🚀</div>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run()