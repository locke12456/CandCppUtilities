import Generator
from CppArg import CppArg
class InterfaceGenerator(object):
    """description of class"""
    filename = ""
    extend = ""
    autoforamt = ""
    cpp = None
    def __init__(self , cpp):
        self.cpp = cpp
        self.filename = cpp.interface[0]
        return
    def Build(self):
        return self._genator_header()
    def _genator_header(self):
        filename = self.filename + ".h"
        hfile = Generator.Generator(filename)
        defineHeader = self.filename.upper()
        hfile.Write("#ifndef __{0}_H__\n".format(defineHeader))
        hfile.Write("#define __{0}_H__\n".format(defineHeader))
        self._write_include(hfile)
        self._write_namespace_begin(hfile)
        hfile.Write("{0}class {1} {2}\n".format(self.autoforamt , self.filename , self.extend))
        hfile.Write("{0}{1}\n".format(self.autoforamt,'{'))
        hfile.Write("{0}public:\n".format(self.autoforamt))
        self._write_constuctor(hfile)
        self._write_deconstructor(hfile)
        hfile.Write("{0}{1};\n".format(self.autoforamt,'}'))
        self._write_namespace_end(hfile)
        hfile.Write("#endif\n".format())
        hfile.Destory()
        return filename
    def _write_constuctor(self,hfile):
        return
    def _write_deconstructor(self,hfile):
        if self.cpp.virtual_decon :
            hfile.Write("{0}{0}virtual ~{1}() = 0;\n".format( self.autoforamt , self.filename ))
    def _write_include(self,hfile):
        return
    def _write_namespace_begin(self,hfile):
        if len(self.cpp.namespace) != 0:
            self.autoforamt = '\t'
            hfile.Write("namespace {0} {1}\n".format(self.cpp.namespace[0] , '{'))
        return
    def _write_namespace_end(self,hfile):
        if len(self.cpp.namespace) != 0:
            hfile.Write("{0}\n".format('};'))
        return

