from pdf2image import convert_from_path

# Convert PDF to a list of images (one per page)
images = convert_from_path("CV_Alexandre_DO_O_ALMEIDA_2025.pdf", dpi=300)

# Save the first page as PNG
images[0].save("CV_Alexandre_DO_O_ALMEIDA_2025.png", "PNG")
