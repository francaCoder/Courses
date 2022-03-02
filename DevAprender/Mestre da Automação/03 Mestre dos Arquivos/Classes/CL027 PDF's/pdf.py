from pikepdf import Pdf

new_pdf = Pdf.new()
with Pdf.open('PDF_Exemplo.pdf') as pdf:
    pdf.save("New Pdf.pdf")
    pdf.close()


# How many pages
with Pdf.open('PDF_Exemplo.pdf') as pdf:
    print(len(pdf.pages))
    pdf.close()


# Delete Pages
with Pdf.open('PDF_Exemplo.pdf') as pdf:
    del pdf.pages[1:2]
    pdf.save("exclusion.pdf")


# Pages
with Pdf.open('PDF_Exemplo.pdf') as pdf:
    how_many_pages = len(pdf.pages)
    new_pdf.pages.append(pdf.pages[0])
    new_pdf.save("New Pdf.pdf")

# Merge
with Pdf.open('PDF_Exemplo.pdf') as pdf:
    source1 = Pdf.open('PDF_Exemplo.pdf')
    source2 = Pdf.open('PDF_Exemplo.pdf')

    pdf.pages.extend(source1.pages)
    pdf.pages.extend(source2.pages)

    pdf.save("Merge PDF.pdf")
    source1.close()
    source2.close()
    pdf.close()


# Password
from pikepdf import Pdf, Permissions, Encryption
with Pdf.open('PDF_Exemplo.pdf') as pdf:
    restrictions = Permissions(extract=False, print_highres=False, modify_form=False)
    pdf.save("Safe Pdf.pdf", encryption=Encryption(user="safe123", allow=restrictions, owner="owner123"))
    pdf.close()