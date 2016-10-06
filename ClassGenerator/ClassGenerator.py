import Generator
import InterfaceGenerator
import HeaderGenertor
import WriteAuthor
from CppArg import CppArg
class ClassGenerator(object):
    """description of class"""
    filename = ""
    extend = ""
    cpp = None
    def __init__(self , cpp ):
        self.cpp = cpp 
        self.filename = cpp.name
        self.SetBaseClass( cpp )
    def SetBaseClass(self , cpp ):
        if len(cpp.interface) == 0 :
            return
        self.extend = cpp.interface[0]
        if self.extend is not None:
            interface = InterfaceGenerator.InterfaceGenerator(cpp)
            interface.Build()
    def Build(self):
        genheader = HeaderGenertor.HeaderGenertor( self.cpp )
        genheader.SetBaseClass( self.cpp )
        header = genheader.Build()
        self._generate_cpp(header)
    def _write_author(self, cpp , cppfile ):
        if cpp.author == "":
            return
        writer = WriteAuthor.WriteAuthor()
        writer.Write( cppfile , cpp )

    def _write_constructor(self, cppfile):
        cppfile.Write("{0}::{0}()\n".format(self.filename))
        cppfile.Write("{\n")
        cppfile.Write("}\n")

    def _write_deconstructor(self, cppfile):
        cppfile.Write("{0}::~{0}()\n".format(self.filename))
        cppfile.Write("{\n")
        cppfile.Write("}\n")
    def _write_method(self,cppfile,type,method):
        cppfile.Write("{0} {1}::{2}()\n".format( type , self.filename , method))
        cppfile.Write("{\n")
        if (type != "void"):
            cppfile.Write("     return {0}();\n".format(type))
        cppfile.Write("}\n")

    def _write_using_namespace(self, cppfile):
        if len(self.cpp.namespace) != 0:
            cppfile.Write("using namespace {0};\n".format(self.cpp.namespace[0]))

    def _generate_cpp(self , header):
        filename = self.filename + ".cpp"
        cppfile  = Generator.Generator(filename)
        self._write_author( self.cpp , cppfile )
        cppfile.Write('#include "{0}"\n'.format(header))
        self._write_using_namespace(cppfile)
        self._write_constructor(cppfile)
        self._write_deconstructor(cppfile)
        cppfile.Destory()


