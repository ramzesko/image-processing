import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import tools


pathcore = 'D:\studia\II stopień\Praca Magisterska\wyniki\\'
folders = ['raw_map', 'averaging_filter_3-3', 'averaging_filter_5-5', 'gaussian_filter_k3', 'gaussian_filter_k5', 'gaussian_filter_k7', 'median_filter_k3', 'median_filter_k5', 'median_filter_k7', 'wiener']
files = ['alpha_map', 'alpha_map_err', 'beta_map', 'beta_map_err']

with open (tools.get_map(files=folders[9], directory=pathcore, extension=files[1]), 'rb') as fp:
    map = pickle.load(fp)
xmap = np.arange(120)
ymap = np.arange(64)
xx, yy = np.meshgrid(xmap, ymap)
z = np.array(map)

# mean = z_alpha.mean()
# to_high = z_alpha>0.0004
# z_alpha[to_high] = 0
# mean = z_alpha[z_alpha<3000].mean()
# print(mean)

mean = z.mean()
#threshold do beta_eff
# mean = z[np.where(np.logical_and(z > 2000, z < 3000))].mean()
# std=np.std(z[np.where(np.logical_and(z > 2000, z < 3000))])
# z_out = np.where(np.logical_or(z < 2000, z > 3000))
# z[z_out] = mean
#####################
# threshold do beta_eff_err
# mean = z[np.where(np.logical_and(z >= 150, z < 700))].mean()
# std=np.std(z[np.where(np.logical_and(z >= 150, z < 700))])
# z_out = np.where(np.logical_or(z <= 150, z > 700))
# z[z_out] = 0
#####################
# threshold do alfa
# mean = z[np.where(np.logical_and(z >= 0.00002, z < 0.00004))].mean()
# std=np.std(z[np.where(np.logical_and(z >= 0.00002, z < 0.00004))])
# z_out = np.where(np.logical_or(z <= 0.00002, z > 0.00004))
# z[z_out] = mean
#####################
# threshold do alfa_err
mean = z[np.where(np.logical_and(z >= 0, z < 0.00002))].mean()
std=np.std(z[np.where(np.logical_and(z >= 0, z < 0.00002))])
z_out = np.where(np.logical_or(z <= 0, z > 0.00002))
z[z_out] = 0

plt.pcolormesh(ymap, xmap, z, cmap='inferno')
sfmt=ticker.ScalarFormatter(useMathText=True)
sfmt.set_powerlimits((0, 0))
bar = plt.colorbar(format=sfmt)
bar.set_label('Dyfuzyjność termiczna [$m^2/s$]', rotation=270, labelpad=20)
plt.axes().set_aspect('equal')
plt.xlim([0,63])
plt.ylim([0,119])
plt.xticks([])
plt.yticks([])
plt.title('filtr medianowy')
# histogram = []
# for i in map:
#     for j in i:
#         if j<5000:
#             histogram.append(j)
# print(histogram)
# plt.hist(histogram, bins='rice')

plt.show()