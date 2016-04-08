# Physical Constants
# Rene' Heller, rheller@astro.physik.uni-goettingen.de, Institute for Astrophysics Goettingen, created 2008-07, last modification 2016-01-12

#from Numeric import *
from pylab import *
from numpy import *
#import numpy
#from futils import rspec
#from phxutils import loadspec
#from phxutils import trapez
#from spectools import scalemodel
#import sys
#import string
#import time
#from matplotlib.font_manager import fontManager, FontProperties
#import pyfits, os, numpy

"""
try:
	from pylab import *
	pylabload = 'y'
except ImportError:
	print "pylab could not be imported."
	pylabload = 'n'

try:
	from matplotlib.font_manager import fontManager, FontProperties
	matplotload = 'y'
except ImportError:
	print "maplotlib features could not be imported."
	matplotload = 'n'

if pylabload == 'n':
	try:
		from numpy import *
	except ImportError:
		print "numpy could not be imported."
"""

G        = 6.673 * 10**(-11.)                              # [m^3 / kg / s^2], Newton's Gravitational constant
h        = 6.626068 * 10.**(-34.)                          # [m^2 * kg / s], Planck constant
hbar     = h/(2*pi)                                        # [m^2 * kg / s], reduced Planck constant
k_B      = 1.3806503 * 10.**(-23.)                         # [m^2 * kg / s^2 / K], Boltzmann constant
c        = 299792458.                                      # [m / s], speed of light
R_gas    = 8.314472 *10**3.                                # [J / K / kg]
R_Gas    = 8.3144621                                       # [J / mol / K]
m_H      = 1.660538921 * 10**(-27.)                        # [kg] mass of a hydrogen atom
m_pro    = 1.672621777 * 10**(-27.)                        # [kg] mass of a proton
m_e      = 9.10938291 * 10.**(-31)                         # [kg], mass of an electron
eV       = 1.60217657 * 10**(-19.)                         # [kg m^2 / s^2], one electron Volt in Joules

sigma_SB = 2. * pi**5. * k_B**4. / (15. * c**2. * h**3.)   # [kg / s^3 / K^4], Stefan-Boltzmann constant
AU       = 149.598 * 10**9.                                # [m], Astronomical Unit

M_sun    = 1.98892*10**30.                                 # [kg], solar mass
M_jup    = 1.8986 * 10**27.                                # [kg], Jupiter mass
M_sat    = 5.6846 * 10**26.                                # [kg], Saturn mass
M_nep    = 1.0243 * 10**26.                                # [kg], Neptune mass
M_ura    = 8.681 * 10**25.                                 # [kg], Uranus' mass
M_mar    = 6.4185 * 10.**23.                               # [kg], Mars' mass
M_ear    = 5.9736 * 10**24.                                # [kg], Earth mass
M_ven    = 4.8676 * 10**24.                                # [kg], Venus' mass
M_mer    = 3.299688 * 10**23.                              # [kg], Mercury's mass

M_gan    = 1.4819  * 10.**23                                # [kg], Ganymede's mass
M_tit    = 1.3452 * 10.**23                                # [kg], Titan's mass
M_cal    = 1.075938 * 10.**23                              # [kg], Callisto's mass
M_io     = 8.931938 * 10.**22                              # [kg], Io's mass
M_moo    = 7.3477 * 10.**22                                # [kg], Moon's mass
M_eur    = 4.799844 * 10.**22                              # [kg], Europa's mass
M_tri    = 2.14   * 10.**22                                # [kg], Triton's mass
M_plu    = 1.305  * 10.**22                                # [kg], Pluto's mass
M_tia    = 3.527 * 10.**21                                 # [kg], Titania's mass
M_obe    = 3.014 * 10.**21                                 # [kg], Oberon's mass
M_rhe    = 2.306518 * 10.**21                              # [kg], Rhea's mass
M_iap    = 1.805635 * 10.**21                              # [kg], Iapetus mass
M_cha    = 1.52 * 10.**21                                  # [kg], Charon's mass
M_ari    = 1.353 * 10.**21                                 # [kg], Ariel's mass
M_umb    = 1.172 * 10.**21                                 # [kg], Umbriel's mass
M_dio    = 1.095452 * 10.**21                              # [kg], Dione's mass
M_enc    = 1.08022 * 10.**20                               # [kg], Enceladus' mass
M_mir    = 6.59 * 10.**19                                  # [kg], Miranda's mass
M_gal    = M_io+M_eur+M_gan+M_cal                          # [kg], total mass of the Galilean moon system

R_sun    = 6.96 * 10**8.                                   # [m], solar radius
R_jup    = (71492000. + 66854000.) / 2.                    # [m], mean of Jupiter's equatorial and polar radius
R_sat    = (60268000 + 54364000) /2.                       # [m], mean of Saturn's equatorial and polar radius
R_nep    = (24764000 + 24341000) /2.                       # [m], mean of Neptune's equatorial and polar radius
R_ura    = (25559. + 24973.) * 1000 / 2.                   # [m], mean of Uranus' equatorial and polar radius
R_ear    = 6378. * 1000.                                   # [m], Earth radius
R_mar    = (3396.2 + 3376.2) * 1000 / 2.                   # [m], mean of Mars' equatorial and polar radius
R_mer    = 2439.7 * 1000                                   # [m], Mercury's radius

R_gan    = 2634.1 * 1000.                                  # [m], Ganymede's radius
R_tit    = 2576.  * 1000.                                  # [m], Titan's radius
R_cal    = 2410.3 * 1000.                                  # [m], Callisto's radius
R_io     = 1821.6 * 1000.                                  # [m], Io's radius
R_moo    = 1737.  * 1000.                                  # [m], Moon radius
R_eur    = 1560.8 * 1000.                                  # [m], Europa's radius
R_tri    = 1353.4 * 1000.                                  # [m], Triton's radius
R_tia    = 788.4 * 1000.                                   # [m], Titania's radius
R_rhe    = 763.8 * 1000.                                   # [m], Rhea's radius
R_obe    = 761.4 * 1000.                                   # [m], Oberon's radius
R_iap    = 734.5 * 1000.                                   # [m], Iapetus' radius
R_umb    = 584.7 * 1000.                                   # [m], Umbriel's radius
R_ari    = 578.9 * 1000.                                   # [m], Ariel's radius
R_dio    = 561.4 * 1000.                                   # [m], Dione's radius
R_enc    = 252.1 * 1000.                                   # [m], Enceladus' radius
R_mir    = 235.8 * 1000.                                   # [m], Miranda's radius

a_mer    = 0.387098    * AU                                # [m], Mercury's semi-major axis with the Sun
a_ven    = 0.723332    * AU                                # [m], Venus' semi-major axis with the Sun
a_mar    = 1.523679    * AU                                # [m], Mars' semi-major axis with the Sun
a_jup    = 5.204267    * AU                                # [m], Jupiter's semi-major axis with the Sun
a_sat    = 9.58201720  * AU                                # [m], Saturn's semi-major axis with the Sun
a_ura    = 19.22941195 * AU                                # [m], Uranus' semi-major axis with the Sun
a_nep    = 30.10366151 * AU                                # [m], Neptune's semi-major axis with the Sun
a_plu    = 39.264 * AU                                     # [m], Pluto's semi-major axis with the Sun
a_mir = 129390000.                                         # [m], orbital distance of Uranus and Miranda
a_moo = 384399000.                                         # [m], orbital distance of the Moon around the Earth
a_io  = 421800000.                                         # [m], orbital distance of Jupiter and Io
a_eur = 671034000.                                         # [m], orbital distance of Jupiter and Europa
a_tit = 1221930000.                                        # [m], orbital distance of Saturn and Titan
a_rhe = 527108000.
a_gan = 1070400000.
a_cal = 1882700000.
a_tri = 354759000.                                         # [m], semi-major axis of Triton's orbit around Neptune
a_obe = 583520000.                                         # [m], semi-major axis of Oberon around Uranus
a_tia = 435910000.                                         # [m], semi-major axis of Titania around Uranus
a_iap = 3560820000.                                        # [m], semi-major axis of Iapetus around Saturn

e_gan = 0.0013
e_tit = 0.0288
e_cal = 0.0074
e_io  = 0.0041                                             # Io's orbital eccentricity about Jupiter
e_moo = 0.0549
e_eur = 0.009
e_tri = 0.000016
e_tia = 0.0011
e_obe = 0.0014
e_rhe = 0.0012583
e_iap = 0.0286125
e_mir = 0.0013

imf_io = 0.02                                              # [1], Io's ice-to-mass fraction
imf_eur = 0.08                                             # [1], Europa's ice-to-mass fraction (referenced in Canup & Ward, 2008, http://arxiv.org/abs/0812.4995)
imf_gan = 0.45                                             # [1], Ganymede's ice-to-mass fraction (referenced in Canup & Ward, 2008, http://arxiv.org/abs/0812.4995)
imf_cal = 0.56                                             # [1], Callisto's ice-to-mass fraction (referenced in Canup & Ward, 2008, http://arxiv.org/abs/0812.4995)
imf_tit = 0.49
rmf_mer = 1-0.6447                                         # [1], Mercury's rock-to-mass fraction (Morgan & Anders, 1980, http://adsabs.harvard.edu/abs/1980PNAS...77.6973M)
rmf_mar = 1.-0.141                                         # [1], Mars' rock-to-mass fraction (Taylor, 2013, http://adsabs.harvard.edu/abs/2013ChEG...73..401T)

T_sun    = 5778.                                           # [K], solar surface or effective temperature
L_sun    = 4. * pi * R_sun**2. * sigma_SB * T_sun**4.      # [W], solar luminosity

min      = 60.                                             # [s], minute in seconds
hr       = 60. * min                                       # [s], hour in seconds
day      = 24. * hr                                        # [s], d in seconds
yr       = 365.25 * day                                    # [s], yr in seconds
Myr      = 10.**6 * yr                                     # [s], Myr in seconds
Gyr      = 10.**9 * yr                                     # [s], Myr in seconds
ly       = c * yr                                          # [m], light year
pc       = AU / sin(1. / 3600. / 180. * pi )

ppm = 10.**(-6.)                                           # [1], parts per million

P_rot_jup = 9.925 * hr                                     # [s], rotation period of Jupiter