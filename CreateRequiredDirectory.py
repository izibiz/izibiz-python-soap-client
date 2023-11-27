import os


def create_directories():
    os.makedirs("Files", exist_ok=True)  # e fatura uygulaması içinv
    os.makedirs("Files/Auth/GetGibUserList", exist_ok=True)
    os.makedirs("Files/EArchive", exist_ok=True)
    os.makedirs("Files/Invoice/GetInvoice", exist_ok=True)
    os.makedirs("Files/Invoice/GetInvoiceWithType", exist_ok=True)
    os.makedirs("Files/GENERATED_XML", exist_ok=True)
    os.makedirs("Required_Files/E_Fatura", exist_ok=True)
    os.makedirs("Required_Files/E_Mustahsil", exist_ok=True)
    os.makedirs("Required_Files/E_Smm", exist_ok=True)
    os.makedirs("Required_Files/XML_CONTENTS", exist_ok=True)
    os.makedirs("Required_Files/XSD", exist_ok=True)
    os.makedirs("Required_Files/E_Arsiv", exist_ok=True)
    os.makedirs("Required_Files/DespatchAdvice", exist_ok=True)
    os.makedirs("Required_Files/DespatchAdvice/SendActions", exist_ok=True)
    os.makedirs("Required_Files/DespatchAdvice/LoadActions", exist_ok=True)
    os.makedirs("Files/DespatchAdvice/getActions", exist_ok=True)

