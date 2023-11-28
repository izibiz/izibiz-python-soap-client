import base64
import random
import re
import uuid
import xml.etree.ElementTree as ET
import zipfile
from datetime import datetime
from Variables import Variable

import requests


class Tools(Variable):

    def FromWsdlToClass(self):

        file = open('require_urls', 'r')
        urls = file.readlines()

        for url in urls:
            url = url.replace('\n', '')
            response = requests.get(url)
            file_name = ""

            if response.status_code == 200:
                text = response.text
                match = re.search(r'tr/(.*?)(\?)', url)
                if match:
                    extracted_text = match.group(1)
                    file_name = str(extracted_text)
                    if '/' in file_name:
                        file_name = file_name.replace('/', '-')
                file = open(f"WSDL/{file_name}", 'w')
                file.write(text)
            else:
                print("WSDL indirme hatası. Durum Kodu:", response.status_code)

    def write_content_to_zip(self, content, type, file_name):

        path = ""
        if type == Variable.GETGIBUSERLIST:
            path = f"Files/Auth/GetGibUserList/get_gib_user_list_scenario_{file_name}.zip"
        elif type == Variable.GETINVOICE:
            path = f"Files/Invoice/GetInvoice/{file_name}.zip"
        elif type == Variable.GETINVOICEWITHTYPE:
            path = f"Files/Invoice/GetInvoiceWithType/{file_name}.zip"
        elif type == Variable.E_ARCHIVE:
            path = f"Files/EArchive/{file_name}.zip"
        if type == Variable.DESPATCHADVICE:
            path = f"Files/DespatchAdvice/getActions/{file_name}.zip"

        file = open(path, 'wb')
        file.write(content)

    def get_session_id(self):

        file = open('session_id', 'r')
        session_id = file.read()
        return session_id

    def display_user_from_zipfle(self, scenario):

        path = f"Files/Auth/GetGibUserList/get_gib_user_list_scenario_{scenario}.zip"
        file_content = ""
        # Zip dosyasını açma (okuma modunda)
        with zipfile.ZipFile(path, "r") as zipf:
            # Zip dosyasındaki dosyalara erişme
            file_list = zipf.namelist()
            # Açmak istenilen dosyanın adı
            target_file = "users"

            if target_file in file_list:
                # Dosyayı zip dosyasından çıkarır ve hedef bir dizine kaydeder
                with zipf.open(target_file) as file:
                    file_content = file.read()
            else:
                print(f"{target_file} zip dosyasında bulunamadı.")
        root = ET.fromstring(file_content)
        user_list = root.findall(".//USER")

        # İlk USER etiketini yazar
        if user_list:
            first_user = user_list[len(user_list) - 1]  # İlk USER etiketi
            identifier = first_user.find("IDENTIFIER").text
            alias = first_user.find("ALIAS").text
            title = first_user.find("TITLE").text
            user_type = first_user.find("TYPE").text
            register_time = first_user.find("REGISTER_TIME").text
            unit = first_user.find("UNIT").text
            document_type = first_user.find("DOCUMENT_TYPE").text
            alias_creation_time = first_user.find("ALIAS_CREATION_TIME").text

            print(f"\n{scenario}. Senaryodaki Son User:")
            print("**********************************************")
            print("IDENTIFIER:", identifier)
            print("ALIAS:", alias)
            print("TITLE:", title)
            print("TYPE:", user_type)
            print("REGISTER_TIME:", register_time)
            print("UNIT:", unit)
            print("DOCUMENT_TYPE:", document_type)
            print("ALIAS_CREATION_TIME:", alias_creation_time)
        else:
            print("USER etiketi bulunamadı.")


    def replace_xml(self, file_path, target_label, new_data):

        tree = ET.parse(file_path)
        root = tree.getroot()
        uuid_element = root.find(target_label)
        uuid_element.text = new_data
        tree.write(file_path)



    def get_time(self):
        # Şu anki tarih, saat ve saniye bilgisi
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def get_date(self):

        # Şu anki tarih ve saat bilgisi
        now = datetime.now()
        current_datetime = now.strftime("%Y-%m-%d")
        return current_datetime

    def display_invoice_header(self, data, service_name):
        invoice = data.invoice[0]
        all_variables = vars(invoice.header)

        print("****************************************************")
        for key, value in all_variables.items():
            print("-\t", key, ":", value)

        print("-\t id:", invoice.id)
        print("-\t list_id:", invoice.list_id)
        print("-\t uuid:", invoice.uuid)

        if invoice.content is None:
            print("-\t content:", invoice.content)
        else:
            if service_name == Variable.GETINVOICE:
                print(f"-\t content: Files/Invoice/GetInvoice/{invoice.uuid}.zip Konumuna Kaydedildi")

                for value in data.invoice[1:]:  # ilk elemandan sonrasını okur.
                    self.write_content_to_zip(value.content.value, Variable.GETINVOICE, value.uuid)

            elif service_name == Variable.GETINVOICEWITHTYPE:
                print(f"-\t content: Files/Invoice/GetInvoiceWithType/{invoice.uuid}.zip Konumuna Kaydedildi")
                self.write_content_to_zip(invoice.content.value, Variable.GETINVOICEWITHTYPE, invoice.uuid)
            else:
                print(f"-\t content: Konum Hatasindan Dolayi Kaydedilemedi")

    def set_loading_content(self):
        random_uuid = str(uuid.uuid4())
        compressed_file = 'compressed.zip'
        element_1 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID"
        element_2 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        random_digit = random.randint(0, 99999)
        random_digit = str(random_digit).zfill(5)

        xml_file_path = "Required_Files/E_Fatura/template.xml"

        self.replace_xml(xml_file_path, element_1, random_uuid)
        self.replace_xml(xml_file_path, element_2, f"MUH{datetime.now().today().year}0000{random_digit}")

        with open(xml_file_path, "rb") as file:
            data = file.read()
        data_base64 = base64.b64encode(data).decode('utf-8')
        return data_base64, random_uuid

    def prepare_loading_content_inZipfile(self, type_name=Variable.E_ARCHIVE):

        random_uuid = str(uuid.uuid4())
        compressed_file = 'compressed.zip'
        element_1 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID"
        element_2 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        random_digit = random.randint(0, 99999)
        random_digit = str(random_digit).zfill(5)

        if type_name == Variable.E_ARCHIVE:

            xml_file_path = "Required_Files/E_Arsiv/deneme.xml"
            self.replace_xml(xml_file_path, element_1, random_uuid)
            self.replace_xml(xml_file_path, element_2, f"SFT{datetime.now().today().year}0000{random_digit}")

            with zipfile.ZipFile(compressed_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(xml_file_path, arcname=xml_file_path)

        if type == Variable.DESPATCHADVICE:

            xml_file_path = "Required_Files/DespatchAdvice/SendActions/template.xml"
            self.replace_xml(xml_file_path, element_1, random_uuid)
            self.replace_xml(xml_file_path, element_2, f"MUH20220000{random_digit}")

            with zipfile.ZipFile(compressed_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(xml_file_path, arcname=xml_file_path)

        with open(compressed_file, "rb") as zip:
            zip_data = zip.read()
        zip_base64 = base64.b64encode(zip_data).decode('utf-8')

        return zip_base64, random_uuid

    def set_loading_content_noZip(self, type_name):
        random_uuid = str(uuid.uuid4())
        compressed_file = 'compressed.zip'
        element_1 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID"
        element_2 = ".//{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        random_digit = random.randint(0, 99999)
        random_digit = str(random_digit).zfill(5)

        xml_file_path = ""

        if type_name == Variable.DESPATCHADVICE:
            xml_file_path = "Required_Files/DespatchAdvice/SendActions/new.xml"
        else:
            xml_file_path = "Files/GENERATED_XML/invoice_xml.xml"

        self.replace_xml(xml_file_path, element_1, random_uuid)
        self.replace_xml(xml_file_path, element_2, f"MUH{datetime.now().today().year}0000{random_digit}")

        with open(xml_file_path, "rb") as file:
            data = file.read()
        data_base64 = base64.b64encode(data).decode('utf-8')

        return data_base64, random_uuid

    def display_response_body(self, response):
        all_variables = vars(response)
        for Key, Value in all_variables.items():
            if Value is not None:
                if Key == "request_return":
                    all_variables = vars(Value)
                    for key, value in all_variables.items():
                        print("-\t", key, ":", value)
                else:
                    print("-\t", Key, ":", Value)
            else:
                print("-\t", Key, ":", Value)

    def display_response_body_for_getMethods(self, response,method):
        all_variables = vars(response)
        for Key, Value in all_variables.items():
            if Value is not None:
                if Key == "despatchadvice":
                    if method =="get_despatch_advice":

                        all_variables = vars(Value[0])
                        for key, value in all_variables.items():
                            if key == "content":
                                print("-\t", key, ":",
                                      f"-Belge Files/DespatchAdvice/{response.despatchadvice[0].uuid}- konumuna kaydedildi")
                            else:
                                print("-\t", key, ":", value)

                        for value in Value[0:]:  # ilk elemandan sonrasını okur.
                            self.write_content_to_zip(value.content.value, Variable.DESPATCHADVICE, value.uuid)

                    elif method =="get_despatch_advice_with_status":
                        if len(Value) != 0:
                            all_variables = vars(Value[0])
                            for key, value in all_variables.items():
                                print("-\t", key, ":", value)
                        else:
                            print("-\t", Key, ":", Value)

                else:
                    print("-\t", Key, ":", Value)
            else:
                print("-\t", Key, ":", Value)



