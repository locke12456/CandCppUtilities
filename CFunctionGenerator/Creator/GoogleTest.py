class GoogleTest(object):
    """description of class"""
    _func = None
    _args = []
    _ret = ""
    _header = ""
    def __init__(self, ret_type = "void" , func = None , arglist = [] ,*args, **kwargs):
        super(GoogleTest, self).__init__(*args, **kwargs)
        self._ret = ret_type
        self._func = func
        self._args = arglist
    def parse(self):
        return 
    def _insert_header_include(self, file, header):
        file.write( '#include "gtest/gtest.h"\n' )
        if header is not None:
            self._header = header
            file.write( '#include "' + header + '.h"\n' )

    def _insert_function_name_to(self, file):
        file.write( "TEST( " + self._header + " , " + self._func + " )\n" )
        

    def _gen_input_or_output(self, arg):
        
        return comment, full_func_name, ret

    def _insert_return_value_to(self , file):
        ret =  "{\n" 
        full_func_name = str(self._func + '( ')
        for arg in self._args:
            t_arg = arg.replace("__IN", "");
            t_arg = t_arg.replace("__OUT", "");
            comment = None
            if arg.replace("__OUT", "") is not arg :
                comment = "/* output */"
            if arg.replace("__IN", "") is not arg :
                comment = "/* input */"
            if comment is not None:
                ret += "    " + t_arg +  ";"+comment +"\n"
            full_func_name += "     "
            full_func_name += t_arg
            if arg is not self._args[len(self._args)-1]:
                 full_func_name += ' , '
            full_func_name += ' '
        full_func_name += ') ;\n'
        
        ret+= "     " + self._ret + " result = " + full_func_name
        ret+= "     ASSERT_EQ( result );\n "
        ret+= "}"
        file.write(ret)

    def generate(self , header = None ):

        file = open( str("T_"+self._func + ".cpp" ) , 'w+')

        self._insert_header_include(file, header)

        self._insert_function_name_to(file)

        self._insert_return_value_to(file)

        file.flush()

        file.close()
        
        return