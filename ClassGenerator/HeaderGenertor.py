import InterfaceGenerator
from CppArg import CppArg
class HeaderGenertor(InterfaceGenerator.InterfaceGenerator):
    """description of class"""
    base = ""
    def __init__(self , cpp):
        self.cpp = cpp
        self.filename = cpp.name
        return
    def SetBaseClass(self , cpp ):
        if len(cpp.interface) == 0 :
            return
        result = len(cpp.interface) != 0
        self.extend = ": public " + cpp.interface[0] if result else base
    def _write_include(self,hfile):
        if( len(self.cpp.interface) != 0 ):
            hfile.Write('#include "{0}.h"\n'.format(self.cpp.interface[0]))
    def _write_constuctor(self, hfile):        
        
        format = self.format + self.autoformat
        hfile.Write("{0}{1}();\n".format( format ,self.filename))
    def _write_deconstructor(self, hfile):
        
        format = self.format + self.autoformat
        if self.cpp.virtual_decon :
            hfile.Write("{0}virtual ~{1}();\n".format( format , self.filename ))
        else:
            hfile.Write("{0}~{1}();\n".format( format , self.filename ))
    def _write_method(self,hfile,type,method):

        format = self.format + self.autoformat
        hfile.Write("{0}virtual {1} {2}();\n".format( format , type , method))
        
