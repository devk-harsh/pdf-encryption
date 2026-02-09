from PyPDF2 import PdfWriter, PdfReader

# Input and output file names
input_file = 'input_file.pdf'
output_file = 'encrypted_file.pdf'

try:
    # Enter the password to encrypt the PDF
    password = input("Enter password to encrypt the PDF: ").strip()
    if not password: # 
        raise ValueError("Password cannot be empty.")
    writer = PdfWriter()

    with open(input_file, 'rb') as file:
        reader = PdfReader(file)
        # Add all pages from the original PDF to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Encrypt the PDF using the provided password
        writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_file, 'wb') as output:
            writer.write(output)
    print("PDF encrypted successfully.")

except FileNotFoundError:
    print(f"Error: {input_file} not found.")

# Catches any unexpected errors
except Exception as e:
    print(f"Error: {e}")
