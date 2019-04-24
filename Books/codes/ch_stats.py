'''
Made on Sun Apr 21 15:04:37 2019
by ysbach
'''
from pathlib import Path

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from matplotlib import rcParams

plt.style.use('default')
rcParams.update({'font.size':12})

from astropy.io import fits
from scipy.stats import chi2

def gaussian(x, mu, sig):
    n = 1 / np.sqrt(2 * np.pi * sig**2)
    return n * np.exp(-1 / 2 * (x - mu)**2 / sig**2)

#%%

if __name__=="__main__":
    fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharex=False, sharey=True, gridspec_kw=None)

    x = np.arange(0, 11, 0.05)
    axg, axc = axs[0], axs[1]

    mu = 4
    sig = 1
    fillwhere = (x >= (mu - sig)) & (x <= (mu + sig))
    pdf_g = gaussian(x, mu, sig)

    axg.plot(x, pdf_g)
    axg.axvline(mu, ls=':', color='r', lw=1)
    axg.axvline(mu - sig, ls=':', color='k', lw=1)
    axg.axvline(mu + sig, ls=':', color='k', lw=1)
    axg.fill_between(x, pdf_g, where=fillwhere,
                     facecolor='none', edgecolor='k', lw=0, hatch='//')
    axg.annotate("area = 1-sigma \n        = 68.27..%",
                 xy=(mu + 1 * sig, 0.25), xytext=(mu + 2 * sig, 0.25),
                 arrowprops=dict(arrowstyle="->"))

    axg.errorbar(mu, 0.45, xerr=sig, capsize=3, marker='o', color='k')
    axg.text(mu, 0.47, r"$4.0 \pm 0.1$", ha='center')
    axg.set_ylim(top=0.5)
    axg.set_title("Gaussian (normal) distribution")
    axg.set_xlabel("Parameter value")
    axg.set_ylabel("pdf")

    dof = 5
    mu = dof - 2
    lo, hi = mu - 2, mu + 3.
    pdf_c = chi2.pdf(x, dof)
    fillwhere = (x >= (lo)) & (x <= (hi))

    axc.plot(x, pdf_c)
    axc.axvline(dof - 2, ls=':', color='r', lw=1)
    axc.axvline(lo, ls=':', color='k', lw=1)
    axc.axvline(hi, ls=':', color='k', lw=1)
    axc.fill_between(x, pdf_c, where=fillwhere,
                     facecolor='none', edgecolor='k', lw=0, hatch='//')

    axc.annotate("area = 1-sigma \n        = 68.27..%",
                 xy=(hi, 0.1), xytext=(hi + 1, 0.1),
                 arrowprops=dict(arrowstyle="->"))
    axc.errorbar(mu, 0.25, xerr=[[2], [3]], capsize=3, marker='o', color='k')
    axc.text(mu, 0.28, r"$3.0^{+3.0}_{-2.0}$", ha='center', fontsize=14)


    axc.set_title("An asymmetric distribution")
    axc.set_xlabel("Parameter value")
    plt.tight_layout()
    plt.savefig(Path("../figs") / "fig_posterior01.png")

#%%
    plt.close('all')
    np.random.seed(123)
    n_measure = 9
    true_mean = 14
    true_std = 0.2

    fig, axs = plt.subplots(2, 1, figsize=(10, 5), sharex=False, sharey=False, gridspec_kw=None)
    for i, n_univ in enumerate([11, 50]):
        ax = axs[i]
        x_arr = np.arange(n_univ)
        in_CI = 0

        for x in x_arr:
            yvals = np.random.normal(true_mean, true_std, size=n_measure)
            if n_univ < 101:
                ax.plot(x.repeat(yvals.shape[0]), yvals, 'xk', alpha=0.5)
                ax.set_ylim(true_mean - 5 * true_std, true_mean + 5 * true_std)
            else:
                ax.set_ylim(true_mean - true_std / 5, true_mean + true_std / 5)
            mean = np.mean(yvals)
            mstd = np.std(yvals, ddof=1) / np.sqrt(yvals.shape[0])
            if np.abs(true_mean - mean) < mstd:
                in_CI += 1
                ax.errorbar(x, mean, yerr=mstd, capsize=3, marker='o', color='r')
            else:
                ax.errorbar(x, mean, yerr=mstd, capsize=3, marker='o', color='b')

        ax.set_xlabel("Universe ID")
        ax.axhline(14)
        ax.set_title(f"n_univ = {n_univ}: {in_CI / n_univ * 100:.1f}% in CI")

    plt.tight_layout()
    plt.savefig(Path("../figs") / "fig_clt01.png")
##%%
#from scipy.stats import t
#nu = 4
#alpha = 0.90
#for alpha in [0.90, 0.95, 0.99]:
#    for nu in [4, 8]:
#        lo, hi = t.interval(alpha=alpha, df=nu)
#        print(f"[{lo:.4f}, {hi:.4f}]", end=' & ')
#    print()
#
#
#
#
#
##%%
#def tstat(m1, m2, s1, s2, n1, n2):
#    num = m1 - m2
#    den = np.sqrt(s1**2 / n1 + s2**2 / n2)
#    return num / den
#
#def dof(s1, s2, n1, n2):
#    num = (s1**2 / n1 + s2**2 / n2)**2
#    den = (s1**2 / n1)**2 / (n1 - 1) + (s2**2 / n2)**2 / (n2 - 1)
#    return num / den
#
#for s2 in [0.1, 0.3,  1.0]:
#    print(s2)
#    print(tstat(14, 15, 0.1 * np.sqrt(5), s2 * np.sqrt(5), 5, 5))
#    print(dof(0.1 * np.sqrt(5), s2 * np.sqrt(5), 5, 5))
#
#t.cdf(-2.1318, df=4)
