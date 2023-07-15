import qrcode as qr
img = qr.make("https://www.buymeacoffee.com/ayushmanmishra")
img.save("BuyMeACoffee.png")