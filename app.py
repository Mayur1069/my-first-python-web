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
                    background-color: #fcfaf5; 
                    color: #1a1a1a;
                    font-family: 'Times New Roman', Times, serif; 
                    margin: 0; 
                    padding: 0;
                    display: flex;
                    justify-content: center;
                }}
                .page-wrapper {{
                    width: 100%;
                    max-width: 850px;
                    padding: 40px 20px;
                    box-sizing: border-box;
                }}
                .document-body {{
                    background: white;
                    padding: 60px 40px;
                    border: 1px solid #ddd;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
                    position: relative;
                    min-height: 100vh;
                }}
                /* The Header */
                .header {{
                    text-align: center;
                    border-bottom: 2px solid #000;
                    padding-bottom: 20px;
                    margin-bottom: 40px;
                }}
                .header h1 {{ margin: 0; font-size: 26px; letter-spacing: 2px; text-transform: uppercase; }}
                .header h2 {{ margin: 10px 0 0; font-size: 18px; font-weight: normal; }}

                /* The Meme Asset */
                .meme-container {{ text-align: center; margin-bottom: 40px; }}
                .meme-container img {{ 
                    width: 100%;
                    max-width: 500px; 
                    border: 2px solid #000;
                }}

                /* Grid for Patent Details */
                .details-grid {{
                    display: grid;
                    grid-template-columns: 1fr;
                    gap: 15px;
                    margin-bottom: 40px;
                    font-size: 15px;
                    background: #f9f9f9;
                    padding: 20px;
                    border: 1px solid #eee;
                }}
                .detail-row {{ display: flex; justify-content: space-between; border-bottom: 1px solid #eee; padding: 5px 0; }}
                .label {{ font-weight: bold; text-transform: uppercase; color: #444; }}

                /* Typography */
                h3 {{ 
                    font-size: 18px; 
                    text-transform: uppercase; 
                    border-bottom: 1px solid #000; 
                    padding-bottom: 5px; 
                    margin-top: 40px; 
                }}
                p, li {{ line-height: 1.7; text-align: justify; font-size: 17px; margin-bottom: 20px; }}
                ul {{ padding-left: 20px; }}
                li {{ margin-bottom: 15px; }}

                /* Signature & Seal */
                .seal {{
                    position: absolute;
                    top: 20px;
                    right: 20px;
                    width: 100px;
                    height: 100px;
                    background: #96281b;
                    border-radius: 50%;
                    color: white;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                    font-size: 11px;
                    font-weight: bold;
                    transform: rotate(15deg);
                    border: 3px dashed white;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                }}
                .footer {{ margin-top: 80px; }}
                .signature-line {{
                    font-family: 'Brush Script MT', cursive;
                    font-size: 40px;
                    border-bottom: 1px solid #000;
                    display: inline-block;
                    padding: 0 40px 5px 0;
                }}

                /* Mobile Adjustments */
                @media (max-width: 600px) {{
                    .page-wrapper {{ padding: 0; }}
                    .document-body {{ padding: 60px 20px; border: none; box-shadow: none; }}
                    .header h1 {{ font-size: 20px; }}
                    .seal {{ width: 80px; height: 80px; font-size: 9px; top: 10px; right: 10px; }}
                    .detail-row {{ flex-direction: column; }}
                }}
            </style>
        </head>
        <body>
            <div class="page-wrapper">
                <div class="document-body">
                    <div class="seal">OFFICIAL<br>BANTER<br>PATENT</div>
                    
                    <div class="header">
                        <h1>OFFICE OF MEMETIC INTELLECTUAL PROPERTY</h1>
                        <h2>CERTIFICATE OF OFFICIAL JOKE PATENT</h2>
                    </div>

                    <div class="meme-container">
                        <img src="{url_for('static', filename='meme1.jpeg')}" alt="Patent Asset">
                    </div>

                    <div class="details-grid">
                        <div class="detail-row"><span class="label">Patent No:</span> <span>MEME-69-420-MK</span></div>
                        <div class="detail-row"><span class="label">Issue Date:</span> <span>January 20, 2026</span></div>
                        <div class="detail-row"><span class="label">Inventor:</span> <span>Mayur Kshirsagar</span></div>
                        <div class="detail-row"><span class="label">Subject:</span> <span>Selective Literacy for High-Volume Textual Interactions</span></div>
                    </div>

                    <h3>I. ABSTRACT</h3>
                    <p>The <strong>"I’m not reading all that shit..."</strong> reaction protocol (hereafter referred to as "The Meme") is a proprietary social maneuver designed to optimize mental energy by refusing to engage with unnecessarily long messages. This patent grants Mayur Kshirsagar exclusive rights to deploy this specific image and text combination within all group chats, Discord servers, and banter-heavy threads.</p>

                    <h3>II. CLAIMS OF OWNERSHIP</h3>
                    <p>The Inventor, Mayur Kshirsagar, hereby claims the following:</p>
                    <ul>
                        <li><strong>The Visual Asset:</strong> The specific depiction of a bandaged, blonde-haired anime youth (Zoro) looking intensely unimpressed.</li>
                        <li><strong>The Verbal Counter:</strong> The precise phrasing of the caption, used as a defensive mechanism against "walls of text."</li>
                        <li><strong>The Contextual Timing:</strong> The right to use this meme exactly 0.5 seconds after a friend sends a deeply detailed or emotional paragraph.</li>
                    </ul>

                    <h3>III. TERMS OF SERVICE & PENALTIES</h3>
                    <p>Any unauthorized use of this joke by friends, family, or acquaintances without prior verbal or written consent from Mayur shall result in:</p>
                    <ul>
                        <li>A formal "L + Ratio" designation.</li>
                        <li>The immediate invalidation of any counter-argument they were trying to make.</li>
                        <li>A requirement to provide Mayur with one (1) beverage or snack of his choice.</li>
                    </ul>

                    <h3>IV. OFFICIAL SEAL</h3>
                    <p>This document is legally binding in the jurisdiction of Humor and Sarcasm. Any attempt to read this entire document in its entirety ironically violates the spirit of the patent itself.</p>

                    <div class="footer">
                        <p>Signed,</p>
                        <div class="signature-line">Mayur Kshirsagar</div>
                        <p style="margin-top: 5px; font-weight: bold;">Chief Executive of Banter</p>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()