# Nixpend


# QR Code Generator and PDF Exporter

This application is a simple Flask-based QR code generator that also exports the generated QR code as a PDF file. Users can input their details in a form, and the application creates a QR code that, when scanned, directs them to a page displaying the submitted details.

## Installation

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the project directory:**

    ```bash
    cd qr_code_generator
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv env
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

5. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Access the application in a web browser at `http://127.0.0.1:5000/`.**

3. **Fill in the form with your details and submit.**

4. **The application generates a QR code that, when scanned, directs you to a page displaying the submitted details.**

5. **To download the PDF containing the QR code, click the download link provided on the page.**

**Note:** Ensure that you use a device capable of scanning QR codes to view the generated page.

## Dependencies

- Flask
- qrcode
- reportlab
