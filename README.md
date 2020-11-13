# EPHEMERIS Non-Sidereal Airmass Module

This module extends the tom_nonsidereal_airmass module to be able to use the
EPHEMERIS scheme of the NON_SIDEREAL target type.

## Usage

To use, clone the repo, and add the path to your PYTHONPATH variable.

Then in your TOM settings.py file, add the line:

    USE_EPHEMERIS_SCHEME = True

This will trigger appropriate code imports in the tom_nonsidereal_airmass
module.
