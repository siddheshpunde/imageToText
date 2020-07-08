from django.shortcuts import render
from django.http import HttpResponse





def function(request):
    return render(request,'function.html')

def uploadImage(request):
    pic=request.FILES['img'];
    from .models import User
    user=User(pic=pic);
    user.save();
    from PIL import Image
    import pytesseract
    import cv2
    from googletrans import Translator
    name=request.FILES['img'].name;
    print(name,"///")
    path='C:/Users/Lenovo/PycharmProjects/webproject/media/profile/'+name
    print(path)
    image = cv2.imread(path, 0)
    print(image)
    lang = "hin+eng+mar+fre+afr+amh+ara+asm+aze+ben+bod+bre+bul+cat+ceb+ces+chi_sim+chi_tra+cos+cym+dan+deu+div+dzo+ell+eng+enm+"+"est+eus+fao+fil+fin+fra+frk+frm+fry+gla+gle+grc+guj+hat+heb+hin+hrv+hye+iku+isl+ita+jpn+kan+kat+kaz+khm+lao+lat+lav+"+"mal+mar+mkd+mlt+mon+mri+msa+nep+nor+oci+ori+osd+pan+rus+san+spn+tam+tur+ukr+urd+uzb"
    text = pytesseract.image_to_string(Image.open(path), lang=lang)
    translator = Translator()
    result = translator.translate(text)
    print(result)
    now = result.text
    html = "<html><body><h1>Text translated result</h1> <p>%s</p></body></html>" % now
    return HttpResponse(html)





