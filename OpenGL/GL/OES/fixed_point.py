'''OpenGL extension OES.fixed_point

This module customises the behaviour of the 
OpenGL.raw.GL.OES.fixed_point to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/fixed_point.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.OES.fixed_point import *
### END AUTOGENERATED SECTION