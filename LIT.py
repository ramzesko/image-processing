import matplotlib.pyplot as plt
import tools
import numpy as np
from scipy.optimize import curve_fit as opt
'''
# 2Hz -----Img413
# 6Hz------Img415
# 10Hz------Img416
# 20Hz-------Img417-418
# 25hz--------Img419
# 30Hz-------Img420
# 35Hz--------Img421
# 40Hz--------Img422
# 45Hz--------Img423
# 50Hz---------Img424
# 55Hz------------Img425
# 60Hz-------------Img426
# 65Hz-------------Img427
# 70Hz--------------Img428
# 75Hz--------------Img429
# 80hz--------------Img430
# 85hz-------------Img431
# 90Hz-------------Img432
# 100Hz------------Img434
# obrazy fazowe to  .ptp
#19 obrazków
'''

files = [413,415,416,417,419,420,421,422,423,424,425,426,427,428,429,430,431,432,434]
freqs = {'413':2,'415':6,'416':10,'417':20,'419':25,'420':30,'421':35,'422':40,'423':45,'424':50,'425':55,'426':60,
         '427':65,'428':70,'429':75,'430':80,'431':85,'432':90,'434':100}
pathcore = r"D:\studia\II stopień\Praca Magisterska\data\\"
extension = r".ptp.csv"

paths = tools.get_paths(files=files, directory=pathcore, extension=extension)
# tools.show_all(paths=paths, directory=pathcore, extension=extension, cmap='inferno')
points =(tools.get_points(paths=paths, coords=(67,29),freqs=freqs, directory=pathcore, extension=extension))
frequencies, svalues = zip(*points)
# print(points)
svalues = np.array(svalues)
plt.plot(frequencies, svalues, '.')
popt, pcov = opt(tools.lit_fit, frequencies, svalues, p0=[2800,30e-6], bounds=([1e-8,1e-8],[np.inf,np.inf]) , method='trf')
perr = np.sqrt(np.diag(pcov))
print('Beta_eff=',popt[0],'+/-',perr[0],'alfa_id=',popt[1],'+/-',perr[1])
x=np.linspace(min(frequencies),max(frequencies),500)
y=tools.lit_fit(x,*popt)
plt.plot(x,y)

plt.title('Beta_eff='+str(round(popt[0],2))+'+/-'+str(round(perr[0],2))+' alfa_id='+str(round(10e5*popt[1],2))+'+/-'+str(round(10e5*perr[1],2))+' *10e-6')
plt.xlabel('Modulation Frequency [Hz]')
plt.ylabel('Phase [deg]')
plt.grid(True)
plt.show()