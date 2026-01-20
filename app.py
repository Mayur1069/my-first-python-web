from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def patent_document():
    return f"""
    <html>
        <head>
            <title>Banter Patent | Official Document</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ 
                    background-color: #f4f1ea; /* Parchment white */
                    font-family: 'Times New Roman', serif; 
                    margin: 0; 
                    padding: 40px;
                    display: flex;
                    justify-content: center;
                }}
                .certificate {{
                    background-color: white;
                    border: 10px double #2c3e50;
                    padding: 50px;
                    max-width: 800px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.2);
                    position: relative;
                }}
                .header {{
                    text-align: center;
                    border-bottom: 2px solid #2c3e50;
                    margin-bottom: 30px;
                }}
                .header h1 {{ margin: 0; font-size: 28px; letter-spacing: 2px; }}
                .header h2 {{ margin: 10px 0; color: #7f8c8d; font-size: 18px; }}
                
                .meme-container {{ text-align: center; margin: 20px 0; }}
                .meme-container img {{ 
                    width: 300px; 
                    border: 3px solid #000;
                    border-radius: 5px;
                }}

                .meta-info {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 10px;
                    margin-bottom: 30px;
                    font-weight: bold;
                }}
                
                h3 {{ border-bottom: 1px solid #bdc3c7; margin-top: 25px; color: #2c3e50; }}
                p {{ line-height: 1.6; text-align: justify; color: #34495e; }}
                ul {{ line-height: 1.8; }}

                .seal {{
                    float: right;
                    width: 100px;
                    height: 100px;
                    background-color: #c0392b;
                    border-radius: 50%;
                    color: white;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                    font-size: 12px;
                    font-weight: bold;
                    transform: rotate(-15deg);
                    border: 4px dashed #922b21;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
                }}
                .signature {{
                    margin-top: 50px;
                    font-family: 'Brush Script MT', cursive;
                    font-size: 30px;
                    border-top: 1px solid #000;
                    display: inline-block;
                    padding-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="certificate">
                <div class="seal">OFFICIAL<br>BANTER<br>SEAL</div>
                
                <div class="header">
                    <h1>OFFICE OF MEMETIC INTELLECTUAL PROPERTY</h1>
                    <h2>CERTIFICATE OF OFFICIAL JOKE PATENT</h2>
                </div>

                <div class="meme-container">
                    <img src="{url_for('static', filename='meme1.jpeg')}" alt="The Patent Asset">
                </div>

                <div class="meta-info">
                    <div>PATENT NO: MEME-69-420-MK</div>
                    <div>ISSUE DATE: January 20, 2026</div>
                    <div>INVENTOR: Mayur Kshirsagar</div>
                    <div>SUBJECT: Selective Literacy</div>
                </div>

                <h3>I. ABSTRACT</h3>
                <p>The "I’m not reading all that shit..." reaction protocol (hereafter referred to as "The Meme") is a proprietary social maneuver designed to optimize mental energy by refusing to engage with unnecessarily long messages. This patent grants Mayur Kshirsagar exclusive rights to deploy this specific image and text combination within all group chats, Discord servers, and banter-heavy threads.</p>

                <h3>II. CLAIMS OF OWNERSHIP</h3>
                <ul>
                    <li><strong>The Visual Asset:</strong> The specific depiction of a bandaged Zoro looking intensely unimpressed.</li>
                    <li><strong>The Verbal Counter:</strong> The precise phrasing of the caption used against "walls of text."</li>
                    <li><strong>The Contextual Timing:</strong> Deployment exactly 0.5 seconds after a long paragraph.</li>
                </ul>

                <h3>III. TERMS & PENALTIES</h3>
                <p>Unauthorized use result in a formal "L + Ratio" designation and the immediate requirement to provide Mayur with one (1) beverage of his choice.</p>

                <h3>IV. OFFICIAL SEAL</h3>
                <p>This document is legally binding in the jurisdiction of Humor and Sarcasm.</p>

                <div class="signature">Mayur Kshirsagar</div>
                <p style="font-size: 12px; margin: 0;">Chief Executive of Banter</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()