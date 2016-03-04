from CppArg import CppArg
class WriteAuthor(object):
    """description of class"""
    def __init__(self, *args, **kwargs):
        return super(WriteAuthor, self).__init__(*args, **kwargs)
    def Write(self ,cppfile, cpp ):
        cppfile.Write("/* \n")
        cppfile.Write(" * File name : {0}\n".format(cpp.name))
        cppfile.Write(" * Author    : {0}\n".format(cpp.author))
        cppfile.Write(" * E-Mail    : {0}\n".format(cpp.email))
        cppfile.Write(" * Language  : C plus plus \n")
        cppfile.Write(" */\n")
        pass

