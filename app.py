from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def gallery():
    return f"""
    <html>
        <head>
            <title>Goa Trip Gallery</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ 
                    background-color: #f0f2f5; 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    margin: 0; 
                    padding: 40px 20px;
                    color: #1c1e21;
                }}
                h1 {{ 
                    margin-bottom: 30px; 
                    font-weight: 300; 
                    letter-spacing: 2px;
                    text-transform: uppercase;
                }}
                .gallery-container {{
                    display: flex;
                    justify-content: center;
                    gap: 30px;
                    flex-wrap: wrap;
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                .photo-card {{
                    background: white;
                    padding: 15px;
                    border-radius: 12px;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                    max-width: 400px;
                }}
                .photo-card:hover {{
                    transform: translateY(-10px);
                    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                }}
                .photo-card img {{
                    width: 100%;
                    height: auto;
                    border-radius: 8px;
                    display: block;
                }}
                .description {{
                    padding: 15px 0 5px 0;
                    font-size: 18px;
                    font-weight: 500;
                    color: #4b4f56;
                }}
                .location {{
                    font-size: 14px;
                    color: #90949c;
                }}
            </style>
        </head>
        <body>
            <h1>🌴 Goa Trip 2026 🌴</h1>
            <div class="gallery-container">
                
                <div class="photo-card">
                    <img src="{url_for('static', filename='goa1.jpeg')}" alt="Trip to Goa">
                    <div class="description">The Best Memories</div>
                    <div class="location">📍 Mandovi River Bridge</div>
                </div>

                <div class="photo-card">
                    <img src="{url_for('static', filename='goa2.jpeg')}" alt="Trip to Goa">
                    <div class="description">Chasing Sunsets</div>
                    <div class="location">📍 North Goa</div>
                </div>

            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()