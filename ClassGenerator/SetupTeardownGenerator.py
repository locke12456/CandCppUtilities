import HeaderGenertor , ClassGenerator , Generator
from CppArg import CppArg
class SetupTeardownGenerator(ClassGenerator.ClassGenerator):
    """description of class"""

    def __init__(self, cpp):
        self.cpp = cpp 
        self.filename = cpp.name
        self.SetBaseClass( cpp )
    
    def Build(self):
        return super(SetupTeardownGenerator, self).Build()

    def _generate_cpp(self , header):
        filename = self.filename + ".cpp"
        cppfile  = Generator.Generator(filename)
        self._write_author( self.cpp , cppfile )
        cppfile.Write('#include "{0}"\n'.format(header))
        self._write_using_namespace(cppfile)
        self._write_constructor(cppfile)
        self._write_deconstructor(cppfile)
        cppfile.Destory()


