'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_detail_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_detail_texture',False)
_p.unpack_constants( """GL_DETAIL_TEXTURE_2D_SGIS 0x8095
GL_DETAIL_TEXTURE_2D_BINDING_SGIS 0x8096
GL_LINEAR_DETAIL_SGIS 0x8097
GL_LINEAR_DETAIL_ALPHA_SGIS 0x8098
GL_LINEAR_DETAIL_COLOR_SGIS 0x8099
GL_DETAIL_TEXTURE_LEVEL_SGIS 0x809A
GL_DETAIL_TEXTURE_MODE_SGIS 0x809B
GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS 0x809C""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLfloatArray)
def glDetailTexFuncSGIS(target,n,points):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetDetailTexFuncSGIS(target,points):pass


def glInitDetailTextureSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
