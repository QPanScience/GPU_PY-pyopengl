'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NVX_conditional_render'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NVX_conditional_render',False)

@_f
@_p.types(None,_cs.GLuint)
def glBeginConditionalRenderNVX(id):pass
@_f
@_p.types(None,)
def glEndConditionalRenderNVX():pass


def glInitConditionalRenderNVX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
