import numpy as np
import matplotlib.pyplot as plt


def get_paths(files, directory, extension):
    paths = []
    for file in files:
        paths.append(directory + 'Image' + str(file) + extension)
    return paths

def show_all(paths, directory, extension, cmap):
    '''
    Possible values of cmap are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2,
#  Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r,
#  Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples,
#  Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2,
#  Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd,
#  YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r,
# coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray,
# gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r,
#  gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r,
#  jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r,
#  rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, terrain, terrain_r, viridis,
#  viridis_r, winter, winter_r
    '''
    fig = plt.figure()
    x = np.arange(64)
    y = np.arange(120)
    for i, path in enumerate(paths):
        ax = fig.add_subplot(5, 4, i + 1)
        img = np.genfromtxt(path, delimiter=',')
        ax.set_title(path[len(directory):-len(extension)])
        cax = ax.pcolormesh(x, y, img, cmap=cmap)
        fig.colorbar(cax)
    plt.show()

def get_points(paths, coords, freqs, directory, extension):
    '''
    coords in range(0-120,0-64)
    '''
    outlist = []
    for path in paths:
        img = np.genfromtxt(path, delimiter=',')
        outlist.append((freqs[str(path[len(directory)+5:-len(extension)])], img[coords[0]][coords[1]]-180))
    return outlist

def lit_fit(f, beta_eff, alfa_id):
    # beta_eff # absorption IR coefficient to fit
    # alfa_id # thermal diffusivity to fit
    alfa_0 = 31e-6
    k_m = 50
    k_g = 0.026
    k_id = 50 # thermal conductivity
    L = 630e-6
    t1 = 1 # instrumental factor
    omega = 2 * np.pi * f
    sigma_t = np.sqrt(1j * omega / alfa_id)
    g = k_g * np.sqrt(alfa_id) / k_id * np.sqrt(alfa_0)
    t = beta_eff / sigma_t
    S_a = (t1 * beta_eff) / (2 * k_m * (beta_eff ** 2 - sigma_t ** 2))
    S_b = 2 * (g + t) - ((t + 1) * (1 + g) * np.exp(sigma_t * L) + (t - 1) * (1 - g) * np.exp(-sigma_t * L)) * np.exp(-beta_eff * L)
    S_c = (1 + g) ** 2 * np.exp(sigma_t * L) - (1 - g) ** 2 * np.exp(-sigma_t * L)
    S = S_a * (S_b / S_c)
    return np.angle(S, deg=True)