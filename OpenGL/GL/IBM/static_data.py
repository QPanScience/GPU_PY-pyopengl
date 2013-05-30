'''OpenGL extension IBM.static_data

This module customises the behaviour of the 
OpenGL.raw.GL.IBM.static_data to provide a more 
Python-friendly API

Overview (from the spec)
	
	The OpenGL specification requires that data be bound at call time.	The
	IBM_static_data extension relaxes the bind-at-call semantics allowing
	an implementation to dereference pointers some time after the
	corresponding calls.
	
	Because of the bind-at-call sematics of standard OpenGL, an
	implementation is required to either copy or fully process data at the
	time it is provided by the application.  Copying data substantially
	increases the demands on the memory subsystem; processing the data may
	result in ineffective amortization of fixed costs.	Neither copying nor
	processing allows multiple rendering threads to operate on the original
	data.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/IBM/static_data.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.IBM.static_data import *
### END AUTOGENERATED SECTION