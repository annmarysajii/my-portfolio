import PyPDF2
import re

def get_links(pdf_path):
    links = []
    try:
        with open(pdf_path, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            for page in pdf.pages:
                if '/Annots' in page:
                    annots = page['/Annots']
                    for annot in annots:
                        try:
                            annot_obj = annot.get_object()
                            if '/A' in annot_obj and '/URI' in annot_obj['/A']:
                                links.append(annot_obj['/A']['/URI'])
                        except Exception as e:
                            pass
    except Exception as e:
        print(f"Error: {e}")
    return links

links = get_links("C:\\Users\\dipuj\\.gemini\\antigravity\\brain\\c14d06b1-de1e-459e-b0a0-b5c562fb0328\\.user_uploaded\\media_1787330729847.pdf")
for link in links:
    print(link)
