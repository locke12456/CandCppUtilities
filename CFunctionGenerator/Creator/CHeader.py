class CHeader(object):
    """description of class"""
    _func = None
    _args = []
    _ret = ""
    def __init__(self, ret_type = "void" , func = None , arglist = [] ,*args, **kwargs):
        super(CHeader, self).__init__(*args, **kwargs)
        self._ret = ret_type
        self._func = func
        self._args = arglist
    def parse(self):
        return 
    def _gen_comment(self, arg):
        
        return ret

    def _insert_function_name_to(self, file):
        ret =  "/*                           \n"
        ret += " * "+ '\\' + "brief  "+self._func+"   \n"
        ret += " *                          \n"
        ret += " * \details comment         \n"
        ret += " *                          \n"
        
        full_func_name = self._ret + '\n' 

        full_func_name+= str(self._func + '(\n')
        for arg in self._args:
            
            t_arg = arg.replace("__IN", "");
            t_arg = t_arg.replace("__OUT", "");
            comment = "[param]"
            if arg.replace("__OUT", "") is not arg :
                comment = "[out]"
            if arg.replace("__IN", "") is not arg :
                comment = "[in]"
            ret += " * \param	"+comment + " " + t_arg + " comment\n"
            full_func_name += "     "
            full_func_name += arg
            if arg is not self._args[len(self._args)-1]:
                 full_func_name += ' , '
            full_func_name += '\n'
        full_func_name += ');\n'

        ret += " */                          \n"
        file.write(ret)
        file.write(full_func_name)


    def generate(self , header = None ):

        file = open( str(header + ".h" ) , 'ab')

        self._insert_function_name_to(file)

        file.flush()
        file.close()
        
        return