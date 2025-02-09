import os
from flask import Flask, request

app = Flask(__name__)

def generate_gmail_variations(base_email, count):
    if "@" not in base_email or ".com" not in base_email:
        return ["Invalid Email"]
    
    prefix, domain = base_email.split("@")
    variations = set()
    
    for i in range(1, count + 1):
        new_email = prefix[:i] + "." + prefix[i:] + "@" + domain
        variations.add(new_email)
    
    return list(variations)

@app.route("/", methods=["GET", "POST"])
def index():
    generated_emails = []
    
    if request.method == "POST":
        base_email = request.form.get("email").strip()
        count = int(request.form.get("count", 1))

        generated_emails = generate_gmail_variations(base_email, count)
    
    return f"""
    <!DOCTYPE html>
    <html lang="hi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gmail Variations Generator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #222;
                color: white;
                text-align: center;
            }}
            input, button {{
                padding: 10px;
                margin: 10px;
                font-size: 18px;
            }}
            .box {{
                background: #333;
                padding: 20px;
                border-radius: 10px;
                display: inline-block;
            }}
            .emails {{
                margin-top: 20px;
            }}
            .emails p {{
                background: #444;
                padding: 10px;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <h2>Gmail Variations Generator</h2>
        <div class="box">
            <form method="POST">
                <label>अपनी असली Gmail डालें:</label><br>
                <input type="email" name="email" required><br>
                <label>कितनी Email Generate करनी है?</label><br>
                <input type="number" name="count" min="1" required><br>
                <button type="submit">Generate करें</button>
            </form>
        </div>

        {"".join(f'<div class="emails"><p>{email}</p></div>' for email in generated_emails) if generated_emails else ""}
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render ke liye port set kar raha hai
    app.run(host="0.0.0.0", port=port)
