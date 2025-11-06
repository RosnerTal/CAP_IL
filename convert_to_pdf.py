from weasyprint import HTML

# Convert the English HTML guide to PDF
HTML('Assets/guide1-english.html').write_pdf('Assets/guide1-english.pdf')
print("✅ English PDF guide created successfully!")

