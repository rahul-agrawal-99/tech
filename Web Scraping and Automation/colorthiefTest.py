from colorthief import ColorThief
import urllib.request 
import os
def dominant_color_from_url(url,tmp_file='tmp.jpg'):
    '''Downloads ths image file and analyzes the dominant color'''
    urllib.request.urlretrieve(url, tmp_file)
    color_thief = ColorThief(tmp_file)
    dominant_color = color_thief.get_color(quality=1)
    os.remove(tmp_file)
    return dominant_color



img_url = 'https://www.freecodecamp.org/news/content/images/size/w2000/2022/09/jonatan-pie-3l3RwQdHRHg-unsplash.jpg'


print(dominant_color_from_url(img_url))