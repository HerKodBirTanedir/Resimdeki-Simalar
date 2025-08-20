# Yüz(Sima) Algılama Uygulaması
## Açıklama
Bu basit Python uygulaması, OpenCV kütüphanesini kullanarak bir resimdeki insan yüzlerini algılar ve bu yüzlerin etrafına bir dikdörtgen çizer. Proje, temel bilgisayarlı görüş (computer vision) yeteneklerini pratik bir şekilde göstermek amacıyla geliştirilmiştir.

## Özellikler
- Temel Yüz Algılama: Bir JPG veya PNG resim dosyasındaki yüzleri algılar.

- Haar Cascade Kullanımı: Yüz algılama için standart ve etkili bir yöntem olan Haar Cascade sınıflandırıcısını kullanır.

- Görsel Geri Bildirim: Algılanan her yüzün etrafına mavi bir dikdörtgen çizerek görsel geri bildirim sağlar.

- Hata Kontrolü: Eksik XML dosyası veya resim gibi yaygın hatalar için kullanıcıya anlaşılır hata mesajları sunar.

## Kurulum
Projeyi yerel makinenizde çalıştırmak için sanal ortam kurmanız ve gerekli kütüphaneleri bu ortama yüklemeniz tavsiye edilir.

## Sanal Ortam Oluşturma ve Etkinleştirme:
Terminalinizi açın ve projenizin ana dizininde aşağıdaki komutları çalıştırın:

```python -m venv sanalortam```

Bu komut, sanalortam adında yeni bir sanal ortam klasörü oluşturur.

## Ortamı etkinleştirmek için:

- Windows:

sanalortam\Scripts\activate

- macOS / Linux:

source sanalortam/bin/activate
Terminalinizin başında (sanalortam) yazdığını gördüğünüzde sanal ortam başarıyla etkinleştirilmiş demektir.

## Gerekli Kütüphaneleri Kurun:
Sanal ortam etkinken, aşağıdaki komutu kullanarak OpenCV ve diğer gerekli kütüphaneleri yükleyin:

```pip install opencv-python```

## Dosyaları Hazırlayın:

- Untitled-1.py adlı Python dosyasını indirin.

- haarcascade_frontalface_default.xml dosyasını aynı dizine ekleyin. Bu dosya, "proje_klasörünüz\sanalortam\Lib\site-packages\cv2\data" klasöründe bulunmaktadır. "haarcascade_frontalface_default.xml" dosyasını proje klasörünüze ekleyiniz yani .py dosyanız ile aynı yerde olsun. Çünkü python kodlarında sadece dosya adını yazarak ulaşacağız. isterseniz "haarcascade_frontalface_default.xml" dosya yolunu ekleyerekde yapabilirsiniz. Eğer "haarcascade_frontalface_default.xml " dosyasını bulamazsanız OpenCV'nin resmi GitHub deposundan bulunabilir.

- Yüzlerini algılamak istediğiniz resim dosyasını (örneğin, ornek_resim.jpg) Python dosyanızla aynı dizine kopyalayın.

## Kullanım
- Untitled-1.py dosyasını bir metin düzenleyici ile açın.

- image_path = 'aile.jpg' satırını bulun ve 'aile.jpg' kısmını kendi resim dosyanızın adıyla değiştirin.

- Terminal veya komut satırını açarak dosyanın bulunduğu dizine gidin.

Uygulamayı sanal ortam etkinken çalıştırmak için aşağıdaki komutu girin:

```python Untitled-1.py```

Başarılı bir şekilde çalıştırdığınızda, yüzleri algılanmış resmi gösteren bir pencere açılacak. Resminizdeki toplam yüz sayısını da terminalde görebilirsiniz.

