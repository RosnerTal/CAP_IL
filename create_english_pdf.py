from xhtml2pdf import pisa

# Read the HTML file
with open('Assets/guide1-english.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Convert HTML to PDF
with open('Assets/guide1-english.pdf', 'wb') as pdf_file:
    pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

if pisa_status.err:
    print(f"Error creating PDF: {pisa_status.err}")
else:
    print("Success! English PDF guide created successfully!")
    print("File saved as: Assets/guide1-english.pdf")

