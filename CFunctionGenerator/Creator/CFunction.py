from Creator.CWriteAuthor import CWriteAuthor
class CFunction(object):
    """description of class"""
    _func = None
    _args = []
    _ret = ""
    def __init__(self, ret_type = "void" , func = None , arglist = [] ,*args, **kwargs):
        super(CFunction, self).__init__(*args, **kwargs)
        self._ret = ret_type
        self._func = func
        self._args = arglist
    def parse(self):
        return 
    def _insert_header_include(self, file, header):
        if header is not None:
            file.write( '#include "{0}.h"\n'.format(header) )

    def _insert_function_name_to(self, file):
        full_func_name = '{0}\n'.format(self._ret ) 
        full_func_name+= str('{0}(\n'.format( self._func ))
        for arg in self._args:
            full_func_name += "\t"
            full_func_name += arg
            if arg is not self._args[len(self._args)-1]:
                 full_func_name += ' , '
            full_func_name += '\n'
        full_func_name += ')'
        file.write(full_func_name)

    def _insert_return_value_to(self , file):
        ret = "{\n" 
        ret+= "\t {0} result ;\n".format(self._ret)
        ret+= "\t return result;\n "
        ret+= "}"
        file.write(ret)

    def generate(self , header = None , auth = None):

        file = open( str(self._func + ".c" ) , 'w+')

        if auth is not None:
            append_writer = CWriteAuthor()
            append_writer.Write( file , auth )

        self._insert_header_include(file, header)

        self._insert_function_name_to(file)

        self._insert_return_value_to(file)

        file.flush()
        file.close()
        return


