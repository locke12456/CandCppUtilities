class CppArg(object):
    namespace = None
    interface = None
    virtual_decon = False
    name = ""
    output_dir = ""
    author = ""
    email = ""
    gtest = False
    gtest_setup_teardown = ""
    def __init__(self, *args, **kwargs):
        super(CppArg, self).__init__(*args, **kwargs)
        self.interface = []
        self.namespace = []
        self.name = ""
        self.author = ""
        self.email = ""
        self.gtest = False
        self.gtest_setup_teardown = ""