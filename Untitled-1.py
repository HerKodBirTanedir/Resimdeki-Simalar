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
image_path = 'aile.jpg' 

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

# Gri tonlamalı resimde yüzleri algılar
# detectMultiScale fonksiyonu, algılanan yüzlerin konumlarını döndürür.
# Parametreler:
# 1.1: scaleFactor - Görüntü ölçeği küçültme oranı. Küçük değerler daha fazla algılama penceresi, daha hassas ama yavaş algılanır.
# 4: minNeighbors - Her adayı kaç komşu dikdörtgenin onaylaması gerektiğini belirler. Yüksek değerler daha az ama daha güvenilir algılama.
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

print(f"Resimde toplam {len(faces)} adet yüz algılandı.")

# Algılanan her yüz için resim üzerinde bir dikdörtgen çiz
for (x, y, w, h) in faces:
    # cv2.rectangle(img(resim), (x, y)sol_üst_köşe, (x + w, y + h)sağ_alt_köşe, (255, 0, 0)renk, (2)çizgi_kalınlığı)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
# İşlenmiş resmi bir pencerede göster
# 'Resimdeki Yüz Algılama' pencerenin başlığı olacak.
cv2.imshow('Resimdeki Yuz Algilama', img)

# Kullanıcının bir tuşa basmasını bekle.
# 0 değeri, herhangi bir tuşa basılana kadar pencerenin açık kalmasını sağlar.
cv2.waitKey(0)

# Tüm OpenCV pencerelerini kapat
cv2.destroyAllWindows()