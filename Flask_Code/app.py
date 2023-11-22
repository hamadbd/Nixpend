from flask import Flask, render_template, request, make_response, url_for
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to display the QR code based on user input
@app.route('/qr')
def qr():
    # Extract parameters from the URL
    name = request.args.get('name')
    email = request.args.get('email')
    telephone = request.args.get('telephone')

    return render_template('result.html', name=name, email=email, telephone=telephone)

# Route to handle form submission and generate QR code + PDF
@app.route('/', methods=['POST'])
def create():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    telephone = request.form['telephone']

    # QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2
    )

    # URL to the page that contains the user's inputs
    url = url_for('qr', name=name, email=email, telephone=telephone, _external=True, _scheme='http')
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code
    qr_filename = f"qr_{name}.png"
    img.save(qr_filename)

    # Generating PDF
    pdf_filename = f"{name}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    data = []

    # Append the QR code inside the PDF
    qr_image = Image(qr_filename, width=400, height=400)
    data.append(qr_image)

    # Create the PDF document
    doc.build(data)

    # Serve the PDF as a response to the user
    with open(pdf_filename, "rb") as pdf_file:
        response = make_response(pdf_file.read())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'inline; filename={pdf_filename}'

    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)