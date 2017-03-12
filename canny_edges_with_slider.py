import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


img = cv2.imread(r'C:\Users\Karol Ramza\Desktop\the_edge.jpg',0)

thres1 = 100
thres2 = 300
edges = cv2.Canny(img,thres1,thres2)

plt.subplot(111)
im = plt.imshow(edges, cmap = 'gray')
plt.title('Canny edges'), plt.xticks([]), plt.yticks([])
plt.subplots_adjust(left=0.15, bottom=0.25)

axcolor = 'lightgoldenrodyellow'
axhte = plt.axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)
axhre = plt.axes([0.15, 0.15, 0.65, 0.03], axisbg=axcolor)

shte = Slider(axhte, 'Threshold Y', 0.1, 1500.0, valinit=300)
shre = Slider(axhre, 'Threshold X', 0.1, 1500.0, valinit=100)

def update(val):
    thres1 = shre.val
    thres2 = shte.val
    edges = cv2.Canny(img, thres1, thres2)
    im.set_data(edges)
    # draw()

shte.on_changed(update)
shre.on_changed(update)

plt.show()