LASTINPUTFILES = []
CWD = ''
DERMETHOD = 'FORWARD'
SECONDDERMETHOD = 'CENTRAL'
INTMETHOD = 'TRAPEZOIDAL'
MAXITERATIONS = 5000
solver = 'numerical'            # solver for the semi analytical model 'numerical' or 'bvp'.

# model constants
OMEGA = 1.4056343e-4            # Angular frequency of the M2 tide (1/s)
G = 9.81                        # Acceleration of gravity (m^2/s)
BETA = 7.6e-4                   # Density conversion for salinity (1/psu)

ALPHA = 1.                      # Constant in quadratic slip BC and k-epsilon turbulence model BC
CMU = 0.09                      # Constant in k-epsilon turbulence model
KAPPA = 0.41                    # Von Karman constant
MOLVIC = 10**(-6)               # Molecular viscosity (m^2/s)
SIGMASAL = 0.7                  # Prandtl-Schmidt number for salinity
RHO0 = 1000.                    # Reference density
RHOS = 2650.                    # Density of ocean
BETAC = 1.-RHO0/RHOS             # Density conversion for sediment
DS = 2.e-5                      # Sediment grain size
R = 0                           # Reference level
TOLERANCEBVP = 1.e-6            # Tolerance of the bvp_solver, i.e. accuracy of the water level solution
sigma_rho = 1
