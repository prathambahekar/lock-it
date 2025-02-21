# importing PyQt6 module
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QPixmap, QPainter, QIcon, QPalette, QColor
# for mica effect
from win32mica import ApplyMica, MicaTheme, MicaStyle
# can use c++ with this
import ctypes
# system modules
import sys
import os

import warnings
warnings.simplefilter("ignore", DeprecationWarning)


