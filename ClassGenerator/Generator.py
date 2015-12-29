from subprocess import call
class Generator(object):
    """description of class"""
    file = None
    def __init__(self , filename = "" ):
        call( ["touch",filename] )
        self.file = open( filename , "w" )
    def Write(self,str):
        self.file.write(str)
        return
    def Destory(self):
        self.file.close()