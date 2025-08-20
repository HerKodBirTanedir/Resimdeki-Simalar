import cv2 # OpenCV ana kütüphanesi
import sys # Programdan kontrollü çıkış yapmak için

# Yüz algılama için Haar Cascade sınıflandırıcısını yükle
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Eğer XML dosyası yüklenemezse kullanıcıya bilgiver ve programı sonlandır
if face_cascade.empty():
    print("HATA: 'haarcascade_frontalface_default.xml' dosyası yüklenemedi!")
    print("Dosyanın kodunuzla aynı dizinde olduğundan veya doğru yolun verildiğinden emin olun.")
    sys.exit() # Programı burada sonlandır

# Algılama yapmak istediğiniz resmin dosya yolunu veya resim dosyanızın adını buraya yazın.
#Resmimiz aynı klasörde olduğu için sadece isim yamanız yeterli.
image_path = 'ornek_resim.jpg' 

# Resmi OpenCV kullanarak yükle
img = cv2.imread(image_path)

# Resim yüklenemezse hata kontrolü yap
if img is None:
    print(f"HATA: Resim dosyası '{image_path}' yüklenemedi!")
    print("Resim adını veya yolunu kontrol edin.")
    sys.exit() # Programı burada sonlandır


# Eğer resminiz çok büyükse ve pencere ekrana sığmıyorsa, bu kısmı kullanabilirsiniz.
# Örneğin, genişliği 800 piksele ayarla ve yüksekliği orantılı olarak küçült.
max_width = 800
if img.shape[1] > max_width: # Eğer resmin genişliği belirlenen maksimum genişlikten büyükse
    oran = max_width / img.shape[1]
    yeni_yukseklik = int(img.shape[0] * oran)
    img = cv2.resize(img, (max_width, yeni_yukseklik))

# Yüz algılama performansı için resmi gri tonlamaya çevir
# Haar Cascade modelleri genellikle gri tonlamalı görüntülerde daha iyi çalışır.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)