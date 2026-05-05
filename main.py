import os
import qrcode
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_generated = False

    # Default values
    upi_id = ""
    name = ""
    amount = ""
    note = ""

    if request.method == "POST":
        upi_id = request.form.get("upi_id")
        name = request.form.get("name")
        amount = request.form.get("amount")
        note = request.form.get("note")

        # Build UPI URL
        upi_url = f'upi://pay?pa={upi_id}&pn={name}&cu=INR'

        if amount:
            upi_url += f'&am={amount}'
        if note:
            upi_url += f'&tn={note}'

        # Ensure static folder exists
        if not os.path.exists("static"):
            os.makedirs("static")

        # Generate QR
        qr = qrcode.make(upi_url).convert("RGB")

        # Add logo in center
        try:
            logo = Image.open("logo.png")
            logo = logo.resize((60, 60))

            pos = (
                (qr.size[0] - logo.size[0]) // 2,
                (qr.size[1] - logo.size[1]) // 2
            )

            qr.paste(logo, pos)
        except:
            pass  # Skip if no logo

        # Save QR
        qr.save("static/qr.png")

        qr_generated = True

    return render_template(
        "index.html",
        qr_generated=qr_generated,
        upi_id=upi_id,
        name=name,
        amount=amount,
        note=note
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)