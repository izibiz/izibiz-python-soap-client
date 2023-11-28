

![İzibiz](https://izibiz.com.tr/wp-content/uploads/2022/11/400dpiLogo_trns.webp)

# İZİBİZ PYTHON SOAP CLİENT
# AÇIKLAMLAR

Bu proje **İzibiz Bilişim Teknolojileri** şirketinin Özel Entegrasyon hizmetleri kapsamında geliştirilmiştir. Gerçekleştirilen bu proje kapsamında;
 - **Kimlik Doğrulama Webservisi**
 - **E-Fatura Webservisi**
 - **E-Arşiv Fatura Webservisi**
 - **E-İrsaliye Webservisi**

 
Webservisleri için **Soap** mimarisi kullanılarak  geliştirme yapılmıştır. Bu Entegrasyon **Python** dili kullanılarak Pycharm idesi üzerinden geliştirilmiştir.

# KURULUM
Eğer entegrasyona yeni başlıyorsanız https://dev.izibiz.com.tr adresi altında ki bilgileri okumanızı tavsiye ederiz.

İlk olarak **https://github.com/izibiz/izibiz-python-soap-client** adresinden projeye ait tüm dosyalar indirilerek oluşturulan python projesine eklenir. Daha sonra **Authorization.py** dosyasının içindeki;
```
  loginRequest.user_name = "kullanici adi giriniz"
  loginRequest.password = "sifre giriniz"
  ```
Alanlarına ilgili kullanıcı adı ve şifre değeri girilir. Daha sonra Authorization.py dosyası koşulur. Projede ilk koşulması gereken dosya Authorization.py dosyasıdır. Token alma işlemi bu sınıfta gerçekleştirilir.  Bu aşamada ayrıca proje boyunca kullanılacak olan dosya dizinleri de oluşturulur.

Her python dosyasında import edilen kütüphaneler belirtilmiştir. Bu kütüphanler kodun başarılı bir şekilde çalışması gereklidir. Kurulum esnasında kodu çalıştırmadan önce bu kütüphanelerin import edilmesi gerekmektedir. İmport işlemi ide yardımıyla gerekli kütüphanenin üzerine tıklanarak otomotik olarak yada farklı yöntemler kullanarak yapılabilir. Ayrıca Python interpreter(yorumlayıcı)'in de eklenmiş olduğuna dikkat edilmelidir.

İlgili uygulamaların çeşitli aşamalarında( örneğin belge yükleme senaryoları gibi) gerekli olacak şablon belgeler **Required_Files** dizini altında her uygulamaya ait dosya içerisinde **template.xml** ismiyle mevcuttur. İstenildiğinde bu şablon belgeler belirtilen dizin üzerinden değiştirilebilir.

## XML Belge Üretmi
Xml belge üretme işlemi oluşturulan xml sınıfları üzerinden gerçekleştirilmektedir. Xml sınıfları **WSDL** dosyaları yardımıyla oluşuturulmaktadır. Gerekli olan WSDL dosyalarına **https://dev.izibiz.com.tr/#webservice-endpoint-wsdl-url78** adresinden erişilebilir. Verilen adreste tüm webservislere ait WSDL dosyaları Webservice Endpoint (WSDL) yani URL şeklinde mevcuttur.

### XML Belge Üretim Aşamaları:
- ilk olarak **xsdata** kütüphanesi Pycharm idesinin terminali üzerinden aşağıdaki komut yardımıyla indirilip kurulur.
```
pip install xsdata[cli,lxml,soap]
```
- Kurulumdan sonra yine terminal üzerinden aşağıdaki komut yardımıyla xml sınıfları elde edilir. Burada örneğin e fatura için xml üretilirse;
```
xsdata  --package paket_ismi  https://efaturatest.izibiz.com.tr/EInvoiceWS?wsdl
```
- Burada ilk parametre kütüphane ismi, ikinci parametre xsd dosyasının yolu ve son parametre ise sınıfların kaydedileceği paket ismidir. burada paket isminden önce **--package** ön ekinin yazılması unutulmamalıdır.

Bu işlem sonucunda terminalde aşağıdakine benzer bir çıktı elde edilir.
>(venv) PS C:\Users\Muhammet\IzibizTestEntegrasyonSoapSide> xsdata  --package paket_ismi  https://efaturatest.izibiz.com.tr/EInvoiceWS?wsdl
>========= xsdata v23.8 / Python 3.11.5 / Platform win32 =========
>Generating package: paket_ismi.efaturatest.izibiz.com.tr.einvoice_ws_wsdl
>Parsing schema https://efaturatest.izibiz.com.tr:443/EInvoiceWS?xsd=4package >paket_ismi  https://efaturatest.izibiz.com.tr/EInvoiceWS?wsdl 
>Parsing schema https://efaturatest.izibiz.com.tr:443/EInvoiceWS?xsd=1
>Compiling schema https://efaturatest.izibiz.com.tr:443/EInvoiceWS?xsd=1
>Builder: 9 main and 0 inner classes
>Builder: 4 main and 0 inner classes
>Analyzer input: 191 main and 105 inner classes
>Analyzer output: 147 main and 102 inner classes
>Generating package: init
>Generating package: init
>Generating package: init
>Generating package: init
>Generating package: init
>Generating package: init
>Generating package: paket_ismi.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_1
>Generating package: paket_ismi.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_2
>Generating package: paket_ismi.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_3
>Generating package: paket_ismi.efaturatest.izibiz.com.tr_443.einvoice_ws_xsd_4
>Generating package: paket_ismi.efaturatest.izibiz.com.tr.einvoice_ws_wsdl

- Bu aşamadan sonra xml sınıfları oluşturulacaktır.
- Daha sonra proje içinde olan **CreateInvoiceXML.py** dosyası gibi xml elementlerinin içeriği doldurulur ve ve elde edilen xml belgesi kaydedilir.
- xml oluştururken **EmbeddedDocumentBinaryObject** elementinin değerlerini kod karmaşıklığı olmaması açısından dosyadan okuyoruz. Bu nedenle **Required_File** dosyası içinde **XML_CONTENTS** dosyası mevcuttur. Bu dosya içerisine  fatura ve müstahsil xml belgesi üretirken kullanılacak **EmbeddedDocumentBinaryObject** elementinin içeriği konulmuştur. **EmbeddedDocumentBinaryObject** elementinin içeri bu dosyalardan okunur. Yada direkt olarak kod üzerinden manuel olarak da bu veri **EmbeddedDocumentBinaryObject** elementine atanabilir.

Oluşturulan xml belgelerin **şematron** kontrolünden geçip geçmediğini görmek için bazı yollar izlenebilir.Örneğin e fatura xml belgesi için şu yol izlenebilir.
e-fatura belge gönderme(sendInvoice) kısmına gidilip 
```
data_base64, random_uuid = self.tools.set_loading_content()
```
satırında bulunan **set_loading_content** metodunun tanımlamasına gidilip e invoice için belge yolu olarak verilen belge yolu yerine oluşan xml belge nereye kaydedildiyse orası yol olarak kullanılabilir.

Servis isteklerini oluştururken **https://dev.izibiz.com.tr** adresindeki bilgiler ve metotların altında yazan açıklama bilgileri dikkatlice okunmalıdır.

WebServis yoğunluğundan dolayı gönderilen isteklere sunucu istenilen sürede (varsayılan olarak 2 saniye ) cevap verememesi durumunda **time out** hataları meydana gelebilir. **time out** hatalarında **xsdata** modülünün **transports** dosyasındaki **DefaultTransport** sınıfında bulunan **timeout** değerinin varsayılan değerini 2.0 dan daha büyük bir değer yapılarak bu hatanın üstesinden gelinebilir.

✨Kolay Gelsin...

