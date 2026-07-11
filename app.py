from flask import Flask

app = Flask(__name__)

click_count = 0

@app.route("/")

def home():
    
    global click_count

    if click_count >= 10:
        bg_color = "#f1c40f" # Celebration Gold
        message = "🎉 BANTER LEVEL: EXPERT! 🎉"
        sub_text = "You've mastered the click. You are a pro."
    else:
        bg_color = "#f4f4f4" # Normal Grey
        message = "Banter Tracker"
        sub_text = f"Keep going! You have clicked {click_count} times."

    return f"""
    <html>
        <body style="text-align: center; font-family: sans-serif; padding-top: 50px; background-color: {bg_color}; transition: background 0.5s;">
            <h1>{message}</h1>
            <p style="font-size: 20px;">{sub_text}</p>

        <a href = "/click">
        
            <button style = "padding: 15px 30px; font-size: 18px; cursor: pointer; background: #2c3e50; color: white; border-radius: 8px;">
            Register Click
            </button>
        </a>

        <br><br>
        <a href = "/reset" style="color: #7f8c8d;">
          Reset Counter  
        </a>
        </body>
    </html>
    """
            

@app.route("/click")

def click():
    
    global click_count
    
    click_count = click_count + 1   

    return """
    
    <html>
        <head>
            <meta http-equiv="refresh" content="0; url=/" />
        </head>
        <body>Redirecting...</body>
    </html>
    """
@app.route("/reset")

def reeset():

    global click_count

    click_count = 0

    return '<meta http-equiv="refresh" content="0; url=/" />'

if __name__ == "__main__":
    app.run()
