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
        result = len(cpp.interface) != 0
        self.extend = ": public " + cpp.interface[0] if result else base
    def _write_constuctor(self, hfile):        
        hfile.Write("{0}{0}{1}();\n".format(self.autoforamt,self.filename))
    def _write_deconstructor(self, hfile):
        if self.cpp.virtual_decon :
            hfile.Write("{0}{0}virtual ~{1}();\n".format( self.autoforamt , self.filename ))
        else:
            hfile.Write("{0}{0}~{1}();\n".format( self.autoforamt , self.filename ))
    def _write_include(self,hfile):
        if( len(self.cpp.interface) != 0 ):
            hfile.Write('#include "{0}"\n'.format(self.cpp.interface[0]))
