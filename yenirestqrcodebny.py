import requests
from datetime import datetime
now = datetime.now()
 # qr code okuma kodu buraya gelecek!
import cv2
import webbrowser
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
 
link = "https://pageloot.com/tr/qr-kod-okuyucu/#live"
 
while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
 
    if data:
        link = data
        break
 
 
    cv2.imshow('QR okuyucu uygulamasi', img)
    if cv2.waitKey(1) == ord('q'):
        break

web = webbrowser.open(str(link))
cap.release()
cv2.destroyAllWindows()


# qr code degeri bu degiskene yazilacak!
qrcode_opncv_ile_okunan = data

# qr code kaydet
r = requests.post(
    "http://127.0.0.1:5000/qrcodes",
    data={
        'code': qrcode_opncv_ile_okunan,
        'title': 'deneme3',
        'date': '%s' % now,
        
    })

print(r.text)

# qr code listesini iste
r = requests.get("http://127.0.0.1:5000/qrcodes")

print(r.text)


