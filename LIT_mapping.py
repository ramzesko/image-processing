import tools
import numpy as np
from scipy.optimize import curve_fit as opt
import pickle


files = [413,415,416,417,419,420,421,422,423,424,425,426,427,428,429,430,431,432,434]
freqs = {'413':2,'415':6,'416':10,'417':20,'419':25,'420':30,'421':35,'422':40,'423':45,'424':50,'425':55,'426':60,
         '427':65,'428':70,'429':75,'430':80,'431':85,'432':90,'434':100}
pathcore = r"D:\studia\II stopień\Praca Magisterska\data\\"
extension = r".ptp.csv"

paths = tools.get_paths(files=files, directory=pathcore, extension=extension)

z_alpha = []
z_beta = []
z_alpha_err = []
z_beta_err = []

for x in range(120):
    row_alpha = []
    row_beta = []
    row_alpha_err = []
    row_beta_err = []
    for y in range(64):
        points =(tools.get_points(paths=paths, coords=(x,y),freqs=freqs, directory=pathcore, extension=extension))
        frequencies, svalues = zip(*points)
        svalues = np.array(svalues)
        try:
            popt, pcov = opt(tools.lit_fit, frequencies, svalues, p0=[2800,30e-6], bounds=([1e-8,1e-8],[np.inf,np.inf]) , method='trf')
            perr = np.sqrt(np.diag(pcov))
            row_alpha.append(popt[1])
            row_beta.append(popt[0])
            row_alpha_err.append(perr[1])
            row_beta_err.append(perr[0])
        except:
            row_alpha.append(0)
            row_beta.append(0)
            row_alpha_err.append(0)
            row_beta_err.append(0)
    z_alpha.append(row_alpha)
    z_beta.append(row_beta)
    z_alpha_err.append(row_alpha_err)
    z_beta_err.append(row_beta_err)
z_alpha = np.array(z_alpha)
z_beta = np.array(z_beta)
z_alpha_err = np.array(z_alpha_err)
z_beta_err = np.array(z_beta_err)
with open('alpha_map', 'wb') as fp:
    pickle.dump(z_alpha, fp)
with open('beta_map', 'wb') as fp:
    pickle.dump(z_beta, fp)
with open('alpha_map_err', 'wb') as fp:
    pickle.dump(z_alpha_err, fp)
with open('beta_map_err', 'wb') as fp:
    pickle.dump(z_beta_err, fp)
