Şifreli Dosya Transfer Uygulaması – AES ve QR Kod Destekli P2P Dosya Paylaşımı

Bu proje, yerel ağ (LAN) üzerindeki cihazlar arasında AES şifrelemeli güvenli dosya transferi sağlar. Kullanıcılar, basit bir grafik arayüz (GUI) ile hem sunucu hem de istemci tarafında işlemleri kolayca yönetebilir. QR kod desteği sayesinde IP adresi paylaşımı hızlı ve pratik hale getirilmiştir.
Özellikler
1. AES Şifreleme ve Çözme

    Dosyalar aktarılmadan önce AES şifrelemesi ile korunur.
    Şifre çözme, istemci tarafında otomatik olarak yapılır.
    Her dosya transferi için yeni bir şifreleme anahtarı üretilir.

2. QR Kod ile IP Paylaşımı

    Sunucu cihaz, QR kod oluşturarak IP adresini paylaşır.
    İstemci cihaz, QR kodu okutarak otomatik bağlanabilir.

3. Basit Grafik Arayüz (GUI)

    Tkinter ile kullanıcı dostu arayüz.
    Tek tıklama ile dosya gönderme ve alma işlemleri yapılabilir.

4. Çoklu Dosya ve İlerleme Takibi (Gelecekte Geliştirilebilir)

    tqdm modülü ile transfer süreci kullanıcıya gösterilir.
    Gelecekte çoklu dosya desteği ve hız optimizasyonu eklenebilir.

Kurulum
Gerekli Kütüphanelerin Yüklenmesi

Projeyi çalıştırmadan önce aşağıdaki Python modüllerini yükleyin:

     bash

     pip install cryptography pillow qrcode tqdm

Proje Dosya Yapısı;


.
├── crypto_utils.py   # AES şifreleme ve çözme fonksiyonları
├── server_gui.py     # Sunucu tarafı dosyası (Dosya gönderimi yapar)
├── client_gui.py     # İstemci tarafı dosyası (Dosya alımı yapar)

Kullanım
1. Sunucu Tarafında (Dosya Göndermek için)

    server_gui.py dosyasını çalıştırın.
    Uygulama, cihazın IP adresini QR kod olarak gösterir.
    QR kodu, istemci cihaz tarafından okutularak IP adresi alınabilir.
    Dosya gönderimi için bir dosya seçin, şifreleme işlemi otomatik olarak yapılır.
    Dosya gönderildikten sonra, istemciye başarılı mesajı gösterilir.

2. İstemci Tarafında (Dosya Almak için)

    client_gui.py dosyasını çalıştırın.
    QR kodu okuyarak veya IP adresini manuel girerek sunucuya bağlanın.
    Bağlantı sağlandığında, dosya aktarımı başlar ve şifresi otomatik çözülür.
    Transfer tamamlandığında başarılı mesajı gösterilir.



             BY YUNUS EMRE YÜKSEL
