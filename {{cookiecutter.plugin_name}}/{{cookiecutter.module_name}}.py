
"""
This module is an example of a barebones function plugin for napari

It implements the ``napari_experimental_provide_function`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from enum import Enum
import numpy as np
from napari_plugin_engine import napari_hook_implementation
import napari

__version__ = "0.0.1"

# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function():
    # we can return a single function
    # or a tuple of (function, magicgui_options)
    # or a list of multiple functions with or without options, as shown here:
    return [threshold]


# Example, a simple function that thresholds an image and creates a labels layer
def threshold(data: napari.types.ImageData, threshold: int) -> napari.types.LabelsData:
    """Threshold an image and return a mask."""
    return (data > threshold).astype(int)

