'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_timer_query'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_timer_query',False)
_p.unpack_constants( """GL_TIME_ELAPSED_EXT 0x88BF""", globals())
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetQueryObjecti64vEXT(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuint64Array)
def glGetQueryObjectui64vEXT(id,pname,params):pass


def glInitTimerQueryEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
