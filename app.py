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
                :root {{
                    --primary-navy: #2c3e50;
                    --paper-color: #fdfcf8;
                }}
                body {{ 
                    background-color: #e0e0e0; 
                    background-image: radial-gradient(#bcbcbc 1px, transparent 1px);
                    background-size: 20px 20px;
                    font-family: 'Times New Roman', Times, serif; 
                    margin: 0; 
                    padding: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: flex-start;
                    min-height: 100vh;
                }}
                .certificate {{
                    background-color: var(--paper-color);
                    border: 2px solid var(--primary-navy);
                    outline: 10px double var(--primary-navy);
                    outline-offset: -20px;
                    padding: 60px;
                    width: 100%;
                    max-width: 800px;
                    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
                    margin: 20px auto;
                    box-sizing: border-box;
                    position: relative;
                }}
                .header {{
                    text-align: center;
                    border-bottom: 3px solid var(--primary-navy);
                    margin-bottom: 40px;
                    padding-bottom: 10px;
                }}
                .header h1 {{ margin: 0; font-size: 32px; letter-spacing: 3px; text-transform: uppercase; }}
                .header h2 {{ margin: 10px 0; color: #555; font-size: 20px; font-style: italic; }}
                
                .meme-container {{ text-align: center; margin: 30px 0; }}
                .meme-container img {{ 
                    width: 100%;
                    max-width: 450px; 
                    border: 4px solid var(--primary-navy);
                    box-shadow: 5px 5px 0px rgba(44, 62, 80, 0.2);
                }}

                .meta-table {{
                    width: 100%;
                    margin-bottom: 30px;
                    font-size: 16px;
                }}
                .meta-table td {{ padding: 5px 0; }}
                .label {{ font-weight: bold; text-transform: uppercase; color: var(--primary-navy); }}
                
                h3 {{ 
                    border-bottom: 1px solid #ccc; 
                    margin-top: 30px; 
                    color: var(--primary-navy); 
                    text-transform: uppercase;
                    font-size: 18px;
                    letter-spacing: 1px;
                }}
                p, li {{ line-height: 1.6; text-align: justify; color: #1a1a1a; font-size: 17px; }}

                .seal {{
                    position: absolute;
                    top: 40px;
                    right: 40px;
                    width: 120px;
                    height: 120px;
                    background-color: #a93226;
                    border-radius: 50%;
                    color: white;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                    font-size: 13px;
                    font-weight: bold;
                    transform: rotate(15deg);
                    border: 5px dashed #7b241c;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
                    z-index: 10;
                }}

                .footer {{
                    margin-top: 60px;
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-end;
                }}
                .signature-block {{ text-align: center; }}
                .signature {{
                    font-family: 'Brush Script MT', cursive;
                    font-size: 38px;
                    border-bottom: 2px solid #000;
                    margin-bottom: 5px;
                    padding: 0 20px;
                }}
                
                @media (max-width: 600px) {{
                    .certificate {{ padding: 30px 20px; outline-width: 5px; outline-offset: -10px; }}
                    .seal {{ width: 80px; height: 80px; font-size: 10px; top: 10px; right: 10px; }}
                    .header h1 {{ font-size: 20px; }}
                }}
            </style>
        </head>
        <body>
            <div class="certificate">
                <div class="seal">OFFICIAL<br>BANTER<br>PROPERTY</div>
                
                <div class="header">
                    <h1>Office of Memetic Property</h1>
                    <h2>CERTIFICATE OF JOKE PATENT</h2>
                </div>

                <div class="meme-container">
                    <img src="{url_for('static', filename='meme1.jpeg')}" alt="Patent Asset">
                </div>

                <table class="meta-table">
                    <tr>
                        <td class="label">Patent No:</td>
                        <td>MEME-69-420-MK</td>
                        <td class="label">Issue Date:</td>
                        <td>January 20, 2026</td>
                    </tr>
                    <tr>
                        <td class="label">Inventor:</td>
                        <td>Mayur Kshirsagar</td>
                        <td class="label">Subject:</td>
                        <td>Selective Literacy</td>
                    </tr>
                </table>

                <h3>I. Abstract</h3>
                <p>The <strong>"I’m not reading all that shit..."</strong> protocol is a proprietary social maneuver designed to optimize mental energy. This patent grants Mayur Kshirsagar exclusive rights to deploy this specific image and text combination within all group chats and banter-heavy threads.</p>

                <h3>II. Claims of Ownership</h3>
                <ul>
                    <li><strong>The Visual Asset:</strong> Depiction of a bandaged Zoro (One Piece) looking unimpressed.</li>
                    <li><strong>The Verbal Counter:</strong> The precise phrasing used against "walls of text."</li>
                    <li><strong>Timing:</strong> Deployment exactly 0.5 seconds after a long message.</li>
                </ul>

                <h3>III. Terms & Penalties</h3>
                <p>Unauthorized use results in a formal "L + Ratio" designation and the requirement to provide the Inventor with one (1) beverage of his choice.</p>

                <div class="footer">
                    <div class="signature-block">
                        <div class="signature">Mayur Kshirsagar</div>
                        <div style="font-weight: bold;">Chief Executive of Banter</div>
                    </div>
                    <div style="font-size: 12px; color: #7f8c8d;">
                        Verified by the Humor & Sarcasm Jurisdiction
                    </div>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()