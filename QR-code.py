import  qrcode 
qr  =  qrcode.QRCode ( 
    version = 1, 
    error_correction= qrcode.ERROR_CORRECT_L, 
    box_size = 10, 
    border = 4, 
) 

qr.add_data ('https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe')

img  =  qr . make_image ( fill_color = "black" ,  back_color = "white" )
img.save('qrcode.png')

from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast("Notification!", "Votre QRcode à bien été crée", threaded=True,
                   icon_path=None, duration=3) 

import time
while toaster.notification_active():
    time.sleep(0.1)