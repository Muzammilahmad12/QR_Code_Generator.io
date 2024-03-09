from django.shortcuts import render
import qrcode
def Home_page(self):
    links=self.POST.get("link")
    image=qrcode.make(str(links))
    image.save("static/image/Link.png")
    img = "static/image/Link.png"
    return render(self,"index.html",{'output' : img})