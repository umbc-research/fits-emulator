import numpy as np
from matplotlib import pyplot as plt
import pprint
import logging
import datetime
import os
from astropy.io import fits

import helper_funcs as hf

params = hf.setArgs()

if not os.path.exists(params.outdir):
    initLog = f"Could not find directory {params.outdir} -- Made directory."
    os.mkdir(params.outdir)

######   LOGGER OBJECT   ######
# Configure logging object, prior to creation
#  Set the filename to be within the specified OUTDIR directory, with date-stamped filename and specific formats
logging.basicConfig(filename='{}/generator_{}.log'.format(params.outdir, datetime.datetime.now().strftime("%Y%m%dT%H%M%S")),\
    encoding='utf-8', format='%(asctime)s %(levelname)s %(message)s', \
    datefmt='%Y%m%dT%H%M%S')

# Actually create the logger object
params.logger = logging.getLogger(__name__)

# Set logging debug level (info isn't as verbose as debug)
if params.level == 'DEBUG':
    params.logger.setLevel(logging.DEBUG)
else:
    params.logger.setLevel(logging.INFO) 

#############################################
####   Print first messages to log
#############################################
params.logger.info(f"Created logger object.")
try:
    params.logger.info(initLog)
except NameError:
    pass
params.logger.info( pprint.pformat(vars(params), indent=1, depth=5) )
params.logger.debug(f"Logger made with debugging level set.")

#############################################
####   Begin!
#############################################

#Generate p point source object positions and total count flux
rPos = np.random.randint(0,params.width,params.pts)
cPos = np.random.randint(0,params.height,params.pts)
totCountsPerSec = np.random.randint(0, 50_000, params.pts)

#Log these positions and total flux counts
for i in range(params.pts):
    params.logger.info(f"Source Position row, col: {rPos[i]}, {cPos[i]} with total flux count: {totCountsPerSec[i]}")

#Create mesh grid on which to calculate source profiles
R, C = np.meshgrid(range(params.height), range(params.width))

#Calculate sigma based on scope, detector, seeing args
sigma = (np.pi * params.focalLength * 1000 * params.seeing /params.pixsize / 180./3600./2.355)

params.logger.info(f"Seeing of {params.seeing}[\'\'/pix] on detector with pixel size {params.pixsize}[um] and on scope with focal len {params.focalLength}[mm] translates to a std of of {sigma}.")

#Create the readnoise frame
darkFrame = np.random.normal(params.readnoise, np.sqrt(params.readnoise), R.T.shape)

#Create the thermal signal frame (scaled with integration time) and add it to the original frame
darkFrame += np.random.normal(params.thermal, np.sqrt(params.thermal), R.T.shape)*params.intTime

flatFrame = hf.pntProfile(C.T, R.T, params.width/2, params.height/2, params.width/1.5, params.height/1.5 )
flatFrame /= np.mean(flatFrame)

#Create a clean light pollution frame scaling the avg sky brightness by the integration time
sourceFrame = np.ones(R.T.shape)*params.pollution * params.intTime

#For each source, scale (based on count flux) a profile centered on 
#    the right location with a sigma from above and scale further by integration time
for i in range(params.pts):
    sourceFrame += totCountsPerSec[i]*hf.pntProfile(C.T, R.T, rPos[i], cPos[i], sigma, sigma)*params.intTime

#Generate a new frame that is a Poisson(Gaussian)-distributed version of the sourceFrame
#  Add the noise frames to this
frameFinal = flatFrame*(np.random.normal(sourceFrame, np.sqrt(sourceFrame), R.T.shape)) + darkFrame

#Save final frame a FITS file
hdu = fits.PrimaryHDU(frameFinal)
hdul = fits.HDUList([hdu])
hdul.writeto(f"{params.outdir}/{params.outdir}_{params.save}.fits")