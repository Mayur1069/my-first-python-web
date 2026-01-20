import random
from flask import Flask

app = Flask(__name__)

roll_history = []

@app.route("/")
def roll_dice():
    global roll_history
    roll = random.randint(1, 20)
    roll_history.insert(0, roll)
    roll_history = roll_history[:5]
    
    history_html = "".join([f"<li>Roll: {r}</li>" for r in roll_history])

    # Default settings
    color = "#2c3e50"
    extra_text = ""  # This starts empty

    # Special logic for rolling a 20
    if roll == 20:
        color = "gold"
        # We add the text and the party popper emoji here
        extra_text = "<h2>🎉 Jay Rutvik! Critical Hit! 🎉</h2>"
    
    if roll == 1:
        color = "red"
        extra_text = "<h2>Critical Fail! 💀</h2>"

    return f"""
    <html>
        <body style="background-color: #f4f4f4; text-align: center; font-family: sans-serif; padding-top: 50px;">
            <h1>D&D Dice Roller</h1>
            
            {extra_text}  <div style="font-size: 100px; color: {color}; font-weight: bold;">{roll}</div>
            
            <button onclick="window.location.reload();" style="padding: 10px; font-size: 20px; cursor: pointer;">Roll Again</button>
            
            <div style="margin-top: 30px; display: inline-block; text-align: left; background: white; padding: 20px; border-radius: 10px; border: 1px solid #ccc;">
                <h3>Recent Roll History:</h3>
                <ul>{history_html}</ul>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()