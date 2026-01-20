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
                    padding: 10px; /* Reduced padding for mobile */
                    display: flex;
                    justify-content: center;
                }}
                .certificate {{
                    background-color: var(--paper-color);
                    border: 2px solid var(--primary-navy);
                    outline: 8px double var(--primary-navy);
                    outline-offset: -15px;
                    padding: 40px 20px; /* Responsive padding */
                    width: 100%;
                    max-width: 800px;
                    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                    margin: 10px auto;
                    box-sizing: border-box;
                    position: relative;
                }}
                .header {{
                    text-align: center;
                    border-bottom: 3px solid var(--primary-navy);
                    margin-bottom: 30px;
                    padding-bottom: 10px;
                }}
                .header h1 {{ margin: 0; font-size: 24px; letter-spacing: 2px; text-transform: uppercase; }}
                .header h2 {{ margin: 5px 0; color: #555; font-size: 16px; font-style: italic; }}
                
                .meme-container {{ text-align: center; margin: 25px 0; }}
                .meme-container img {{ 
                    width: 100%;
                    max-width: 400px; 
                    border: 3px solid var(--primary-navy);
                }}

                /* Grid instead of Table for better mobile flow */
                .meta-grid {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 15px;
                    margin-bottom: 25px;
                    font-size: 14px;
                    border: 1px solid #ddd;
                    padding: 15px;
                    background: rgba(0,0,0,0.02);
                }}
                .meta-item {{ display: flex; flex-direction: column; }}
                .label {{ font-weight: bold; text-transform: uppercase; color: var(--primary-navy); font-size: 11px; }}
                
                h3 {{ 
                    border-bottom: 1px solid #ccc; 
                    margin-top: 25px; 
                    color: var(--primary-navy); 
                    text-transform: uppercase;
                    font-size: 16px;
                }}
                p, li {{ line-height: 1.5; text-align: justify; color: #1a1a1a; font-size: 16px; }}

                .seal {{
                    position: absolute;
                    top: 15px;
                    right: 15px;
                    width: 90px;
                    height: 90px;
                    background-color: #a93226;
                    border-radius: 50%;
                    color: white;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                    font-size: 10px;
                    font-weight: bold;
                    transform: rotate(15deg);
                    border: 4px dashed #7b241c;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.2);
                    z-index: 10;
                }}

                .footer {{
                    margin-top: 40px;
                    display: flex;
                    flex-direction: column; /* Stacked for mobile */
                    align-items: center;
                    gap: 20px;
                }}
                .signature-block {{ text-align: center; }}
                .signature {{
                    font-family: 'Brush Script MT', cursive;
                    font-size: 32px;
                    border-bottom: 2px solid #000;
                    margin-bottom: 5px;
                    padding: 0 30px;
                }}
                
                /* Tablet and Desktop adjustments */
                @media (min-width: 600px) {{
                    .certificate {{ padding: 60px; outline-width: 10px; outline-offset: -20px; }}
                    .header h1 {{ font-size: 32px; }}
                    .seal {{ width: 120px; height: 120px; font-size: 13px; top: 40px; right: 40px; }}
                    .footer {{ flex-direction: row; justify-content: space-between; align-items: flex-end; }}
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

                <div class="meta-grid">
                    <div class="meta-item"><span class="label">Patent No:</span>MEME-69-420-MK</div>
                    <div class="meta-item"><span class="label">Issue Date:</span>Jan 20, 2026</div>
                    <div class="meta-item"><span class="label">Inventor:</span>Mayur Kshirsagar</div>
                    <div class="meta-item"><span class="label">Subject:</span>Selective Literacy</div>
                </div>

                <h3>I. Abstract</h3>
                <p>The <strong>"I’m not reading all that shit..."</strong> protocol is a proprietary social maneuver designed to optimize mental energy. This patent grants Mayur Kshirsagar exclusive rights to deploy this specific image and text combination within all group chats and banter-heavy threads.</p>

                <h3>II. Claims of Ownership</h3>
                <ul>
                    <li><strong>The Visual Asset:</strong> Depiction of a bandaged Zoro looking intensely unimpressed.</li>
                    <li><strong>The Verbal Counter:</strong> The precise phrasing used against "walls of text."</li>
                </ul>

                <div class="footer">
                    <div class="signature-block">
                        <div class="signature">Mayur Kshirsagar</div>
                        <div style="font-weight: bold;">Chief Executive of Banter</div>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()