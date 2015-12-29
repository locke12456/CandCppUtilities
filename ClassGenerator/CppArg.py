class CppArg(object):
    namespace = None
    interface = None
    virtual_decon = False
    name = ""
    output_dir = ""
    def __init__(self, *args, **kwargs):
        super(CppArg, self).__init__(*args, **kwargs)
        self.interface = []
        self.namespace = []
        self.name = ""