import random  # This library helps us generate random numbers
from flask import Flask

app = Flask(__name__)

@app.route("/")
def roll_dice():
    # Generate a random number between 1 and 20 (a d20!)
    roll = random.randint(1, 20)
    
    # Choose a color based on the roll (Red for 1, Gold for 20)
    color = "#2c3e50"
    if roll == 1: color = "red"
    if roll == 20: color = "gold"

    return f"""
    <html>
        <body style="background-color: #f4f4f4; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding-top: 100px;">
            <h1 style="color: #333;">D&D Dice Roller</h1>
            <div style="font-size: 120px; color: {color}; margin: 20px;">
                {roll}
            </div>
            <p style="font-size: 20px;">You rolled a <strong>d20</strong>!</p>
            <button onclick="window.location.reload();" style="padding: 10px 20px; font-size: 16px; cursor: pointer;">Roll Again</button>
            <br><br>
            <small>Refresh the page to roll again.</small>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()