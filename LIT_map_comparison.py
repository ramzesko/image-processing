import pickle
import numpy as np
import matplotlib.pyplot as plt
import tools


pathcore = 'D:\studia\II stopień\Praca Magisterska\wyniki\\'
# folders = ['raw_map', 'averaging_filter_3-3', 'averaging_filter_5-5', 'gaussian_filter_k3', 'gaussian_filter_k5', 'gaussian_filter_k7']
folders = ['raw_map', 'averaging_filter_3-3', 'averaging_filter_5-5', 'gaussian_filter_k3', 'gaussian_filter_k5', 'gaussian_filter_k7', 'median_filter_k3', 'median_filter_k5', 'median_filter_k7', 'wiener']
files = ['alpha_map', 'alpha_map_err', 'beta_map', 'beta_map_err']

maps = []
for filter in folders:
    with open (tools.get_map(files=filter, directory=pathcore, extension=files[1]), 'rb') as fp:
        maps.append(pickle.load(fp))
xmap = np.arange(120)
ymap = np.arange(64)
fig = plt.figure()

for i, map in enumerate(maps):
    ax = fig.add_subplot(5, 2, i + 1)
    z = np.array(map)
    # narysowanie beta wymaga thresholdu, ponieważ są duże błędy
    mean = z.mean()
    std = np.std(z)
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
    #####################
    print(folders[i], ': ', mean, '+/-', std)
    ############################################################
    ax.set_title(folders[i])
    cax = ax.pcolormesh(ymap, xmap, z, cmap='inferno')
    fig.colorbar(cax)
    ax.set_xlim([0,63])
    ax.set_ylim([0,119])
#histogram błędów
    # ax.hist(z[np.where(np.logical_and(z >= 150, z < 700))], bins='scott') #beta
    # ax.hist(z[np.where(np.logical_and(z > 0, z < 0.00002))], bins='scott') #alfa
    # ax.set_xlim([0,0.00002])

plt.show()