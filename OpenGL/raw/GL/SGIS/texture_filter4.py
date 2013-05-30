'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_texture_filter4'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_texture_filter4',False)
_p.unpack_constants( """GL_FILTER4_SGIS 0x8146
GL_TEXTURE_FILTER4_SIZE_SGIS 0x8147""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexFilterFuncSGIS(target,filter,weights):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,arrays.GLfloatArray)
def glTexFilterFuncSGIS(target,filter,n,weights):pass


def glInitTextureFilter4SGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
