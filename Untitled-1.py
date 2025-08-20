import cv2 # OpenCV ana kütüphanesi
import sys # Programdan kontrollü çıkış yapmak için

# Yüz algılama için Haar Cascade sınıflandırıcısını yükle
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Eğer XML dosyası yüklenemezse kullanıcıya bilgiver ve programı sonlandır
if face_cascade.empty():
    print("HATA: 'haarcascade_frontalface_default.xml' dosyası yüklenemedi!")
    print("Dosyanın kodunuzla aynı dizinde olduğundan veya doğru yolun verildiğinden emin olun.")
    sys.exit() # Programı burada sonlandır
