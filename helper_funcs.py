import argparse
import numpy as np
import sys

#############################################
####   Dummy Class to hold vars
#############################################
class params:
    pass

def setArgs():
    #############################################
    ####   Create Argument Parser and Parse!
    #############################################
    description = \
    """
    FITS File Emulator for point sources
    """

    parser = argparse.ArgumentParser(\
                        prog='fits-emulator', allow_abbrev=True,\
                        description=description,\
                        epilog='Submit github issue with any quesitons or concerns.')

    ## OPTIONAL ARGUMENTS
    #Set logging level
    parser.add_argument('--level', '-level', metavar="INFO|DEBUG", \
                        action="store", required=False, \
                        help="Set Logging level to either INFO or DEBUG",\
                        choices=['INFO', 'DEBUG'], default='INFO')


    # Specify number of frames to generate
    parser.add_argument("--number", '-n', metavar="int", action="store", type=int, required=False, default=1,\
                        help="DEFAULT is 1.\nNumber of frames to generate with same field parameters, separated by dt",\
                        )
    
    # Specify number of seconds between frames to generate
    parser.add_argument("--dt", '-dt', metavar="float", action="store", type=int, required='--number' in sys.argv or '-n' in sys.argv,\
                        help="Number of seconds between frames\nOnly required if --number > 1",\
                        )

    # Specify number of calibration frames to generate
    parser.add_argument("--ncalibration", '-c', metavar="int", action="store", type=int, required=False, default=1,\
                        help="DEFAULT IS 1.\nNumber of calibration frames to take.",\
                        )
    
    # Specify number of frames to generate
    parser.add_argument("--nframes", metavar="int", action="store", type=int, required=False, default=1,\
                        help="DEFAULT IS 1.\nNumber of light frames to take.",\
                        )

    # Specify Version flag
    parser.add_argument('--version', '-V', '-version', action='version', version='%(prog)s Version 1.0, 20240303')

    ## REQUIRED ARGUMENTS
    required = parser.add_argument_group('required arguments')

    # Save Flag
    required.add_argument('--save', default="", action='store', metavar="title",\
                        help="Save FITS of frame",\
                        type=str
                        )
    
    # Specify exposure time
    required.add_argument("--intTime", '-t', metavar="float", action="store", type=float, required=True,\
                        help="Integration time in s",\
                        )

    # Specify focal length
    required.add_argument("--focalLength", '-f', metavar="float", action="store", type=float, required=True,\
                        help="Focal length in mm",\
                        )

    # Specify pixel size
    required.add_argument("--pixsize", '-s', metavar="float", action="store", type=int, required=True,\
                        help="Pixel Size in um (micron)",\
                        )

    # Specify lower seeing bound
    required.add_argument("--seeing", metavar="float", action="store", type=int, required=True,\
                        help="Specify lower bound of seeing in arcsec",\
                        )

    # Specify background light pollution in average counts/sec
    required.add_argument("--pollution", metavar="float", action="store", type=int, required=True,\
                        help="Specify background light pollution in average counts/sec",\
                        )

    # Specify thermal signal in average counts/sec
    required.add_argument("--thermal", metavar="float", action="store", type=int, required=True,\
                        help="Specify thermal signal in average counts/sec",\
                        )

    # Specify readnoise in counts/pixel
    required.add_argument("--readnoise", metavar="float", action="store", type=int, required=True,\
                        help="Specify readnoise in counts/pixel",\
                        )

    # Specify number of point sources to generate
    required.add_argument("--pts", '-p', metavar="int", action="store", type=int, required=True,\
                        help="Number of point sources to generate",\
                        )

    # Specify output directory
    required.add_argument("--outdir", '-O', '-outdir', metavar="dir", action="store", type=str, required=True,\
                        help="Directory where log and new FITS will be written.",\
                        )

    # Specify width of frame
    required.add_argument("--width", '-W', '-width', metavar="int", action="store", type=int, required=True,\
                        help="Number of pixels in horizontal dimensions",\
                        )
    
    # Specify height of frame
    required.add_argument("--height", '-H', '-height', metavar="int", action="store", type=int, required=True,\
                        help="Number of pixels in vertical dimensions",\
                        )

    parser.parse_args(namespace=params)
    return params

def pntProfile(x, y, mux, muy, sx, sy):
    return 1./ sx/sy/2*np.pi * np.exp( -(((x-mux)**2)/sx/sx + ((y-muy)**2)/sy/sy)/4)