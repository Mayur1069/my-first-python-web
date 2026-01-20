import random
from flask import Flask

app = Flask(__name__)

# This list will store our rolls in the server's memory
roll_history = []

@app.route("/")
def roll_dice():
    global roll_history
    roll = random.randint(1, 20)
    
    # Add the new roll to the start of our list
    roll_history.insert(0, roll)
    
    # Keep only the last 5 rolls
    roll_history = roll_history[:5]
    
    # Create the HTML for the history list
    history_html = "".join([f"<li>Roll: {r}</li>" for r in roll_history])

    color = "#2c3e50"
    if roll == 1: color = "red"
    if roll == 20: color = "gold"

    print("Rutvik is chocolate boy")

    return f"""
    <html>
        <body style="background-color: #f4f4f4; text-align: center; font-family: sans-serif; padding-top: 50px;">
            <h1>D&D Dice Roller</h1>
            <div style="font-size: 100px; color: {color};">{roll}</div>
            <button onclick="window.location.reload();" style="padding: 10px; font-size: 20px;">Roll Again</button>
            
            <div style="margin-top: 30px; display: inline-block; text-align: left; background: white; padding: 20px; border-radius: 10px; border: 1px solid #ccc;">
                <h3>Recent Roll History:</h3>
                <ul>{history_html}</ul>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()