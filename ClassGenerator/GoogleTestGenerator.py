import ClassGenerator , Generator
import WriteAuthor
from CppArg import CppArg
class GoogleTestGenerator(ClassGenerator.ClassGenerator):
    """description of class"""
    def __init__(self, cpp):
        super(GoogleTestGenerator, self).__init__(cpp)
        self.cpp = cpp 
        self.filename = "T_"+cpp.name

    def Build(self):
        self._generate_cpp(self.cpp.gtest_setup_teardown)

    def _generate_cpp(self , header):
        filename = self.filename + ".cpp"
        cppfile  = Generator.Generator(filename)
        self._write_author( self.cpp , cppfile )
        cppfile.Write('#include "gtest/gtest.h"\n'.format(header))
        cppfile.Write('#include "{0}.h"\n'.format(self.cpp.name))
        cppfile.Write('#include "{0}.h"\n'.format(header))
        self._write_using_namespace(cppfile)
        self._write_gtest(cppfile)
        cppfile.Destory()
    
    def _write_gtest(self, cppfile):
        cppfile.Write("/*                                                                                                                \n")
        cppfile.Write(" *  {0}                                                                                                           \n".format(self.cpp.name))
        cppfile.Write(" */                                                                                                               \n".format(self.cpp.name))
        cppfile.Write("class T_{0} :                                                                                                     \n".format(self.cpp.name))
        cppfile.Write("     public {0} , public testing::WithParamInterface<AssertValue>                                                 \n".format(self.cpp.gtest_setup_teardown))
        cppfile.Write("{                                                                                                                 \n")
        cppfile.Write("public:                                                                                                           \n")
        cppfile.Write("    T_{0}();                                                                                                      \n".format(self.cpp.name))
        cppfile.Write("                                                                                                                  \n")
        cppfile.Write("    testing::AssertionResult Assert{0}(const char* Value_exp, AssertValue Value);  \n".format(self.cpp.name))
        cppfile.Write("};                                                                                                                \n")
        
        cppfile.Write("AssertionResult T_{0}::Assert{0}(const char* Value_exp, AssertValue Value)   \n".format(self.cpp.name))
        cppfile.Write("{\n")
        cppfile.Write("     Message msg( {1} {0} {1} );\n".format("NOT IMPL",'"'))
        cppfile.Write("     AssertValue result;\n")
        cppfile.Write("     {0}::{1}* test = new {0}::{1}();\n".format(self.cpp.namespace[0],self.cpp.name))
        cppfile.Write("     return (result == Value) ? AssertionSuccess() : AssertionFailure(msg);\n")        
        cppfile.Write("}\n")
        cppfile.Write("TEST_F(T_{0},{0}_Case_1)\n".format(self.cpp.name))
        cppfile.Write("{\n")
        cppfile.Write("     AssertValue Value;\n")
        cppfile.Write("     EXPECT_PRED_FORMAT1(Assert{0}, Value);\n".format(self.cpp.name))
        cppfile.Write("}\n")

