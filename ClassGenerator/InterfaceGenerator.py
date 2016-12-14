import Generator
import WriteAuthor
from CppArg import CppArg
class InterfaceGenerator(object):
    """description of class"""
    filename = ""
    extend = ""
    autoformat = ""
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
        self._write_author( self.cpp , hfile )
        defineHeader = self.filename.upper()
        hfile.Write("#ifndef __{0}_H__\n".format(defineHeader))
        hfile.Write("#define __{0}_H__\n".format(defineHeader))
        self._write_include(hfile)
        self._write_namespace_begin(hfile)
        hfile.Write("{0}class {1} {2}\n".format(self.format , self.filename , self.extend))
        hfile.Write("{0}{1}\n".format(self.format,'{'))
        hfile.Write("{0}public:\n".format(self.format))
        self._write_constuctor(hfile)
        self._write_deconstructor(hfile)
        hfile.Write("{0}{1};\n".format(self.format,'}'))
        self._write_namespace_end(hfile)
        hfile.Write("#endif\n".format())
        hfile.Destory()
        return filename
    def _write_author(self, cpp , cppfile ):
        if cpp.author == "":
            return
        writer = WriteAuthor.WriteAuthor()
        writer.Write( cppfile , cpp )
    def _write_constuctor(self,hfile):
        return
    def _write_deconstructor(self,hfile):
        if self.cpp.virtual_decon :
            hfile.Write("{0}{0}virtual ~{1}() {2};\n".format( self.autoformat , self.filename ,'{}'))
    def _write_include(self,hfile):
        return
    def _write_namespace_begin(self,hfile):
        if len(self.cpp.namespace) != 0:
            self.autoformat = '\t'
            arr = self.cpp.namespace[0].split("::")
            
            self.format = ""
            for cnt in range(0,len(arr)):
                namespace = arr[cnt]
                hfile.Write("{0}namespace {1} {2}\n".format(self.format, namespace , '{'))
                if cnt < len(arr):
                    self.format += self.autoformat
        return
    def _write_namespace_end(self,hfile):
        arr = self.cpp.namespace[0].split("::")
        
        self.format = ""
        for cnt in range(0,len(arr)):
            for tab in range(cnt+1,len(arr)):
                self.format += self.autoformat
            hfile.Write("{0}{1}\n".format(self.format,'};'))
            self.format = ""
        return

