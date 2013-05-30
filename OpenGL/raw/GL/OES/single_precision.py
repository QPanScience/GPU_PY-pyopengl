'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_OES_single_precision'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_single_precision',False)

@_f
@_p.types(None,_cs.GLclampf,_cs.GLclampf)
def glDepthRangefOES(n,f):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glFrustumfOES(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glOrthofOES(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glClipPlanefOES(plane,equation):pass
@_f
@_p.types(None,_cs.GLclampf)
def glClearDepthfOES(depth):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetClipPlanefOES(plane,equation):pass


def glInitSinglePrecisionOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
