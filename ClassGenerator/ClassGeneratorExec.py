## 
## Author : Locke Chen
## E-Mail : locke12456@gmail.com
## Language: Python2
## 
import ClassGenerator , GoogleTestGenerator
import CppArg
import getopt
import sys
import argparse
import os

def usage():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a','--author', help=' ')
    parser.add_argument('-e','--email', help=' ')
    parser.add_argument('-I','--interface', help=' ')
    parser.add_argument('-N','--namespace', help=' ')
    parser.add_argument('-n','--name', help='class name . e.g. -n file ')
    parser.add_argument('-v','--virtual_decon', help='class has virtual deconstuctor . ')
    parser.add_argument('-o','--output_dir', help='output directory. e.g. -o path ')
    parser.add_argument('-G','--google_test', help='unit test ')
    parser.add_argument('-s','--setup_teardown', help='unit test setup and teardown file.')

    try:
        parser.print_usage()
    except:
        print ""
    print "usage example : python ClassGeneratorExec.py -I IMqtt -v 1 -N Mqtt -n MqttInstance "
    

def set_name(cpp,val):
    cpp.name = val
def split_namespace(cpp,arg):
    cpp.namespace = cpp.namespace.split("::")

def mapping_args( opts , cpp):
    output = None
    interface_opt = (lambda opt,arg : cpp.interface.append(arg) )
    namespace_opt = (lambda opt,arg : cpp.namespace.append(arg) )
    name_opt = (lambda opt,arg : set_name(cpp,arg) )
    
    options = {"-I" :  interface_opt , "-N" : namespace_opt , "-n" : name_opt  }   
    
    for opt, arg in opts:  
        if opt in ("-o", "--output"):
            cpp.output_dir = arg
            continue  
        if opt in ("-v", "--virtual_decon"):
            cpp.virtual_decon = True
            continue  
        if opt in ("-a","--author"):
            cpp.author = arg
            continue
        if opt in ("-e","--email"):
            cpp.email = arg
            continue
        if opt in ("-G","--google_test"):
            cpp.gtest = True
            continue
        if opt in ("-s","--setup_teardown"):
            cpp.gtest_setup_teardown = arg
            continue
        if opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        if options.has_key(opt):
            options[opt](opt,arg)
    return output
def main(argv):
    dir = os.getcwd() + "\\ouput\\"

    try:                                
        opts, args = getopt.getopt(argv, "hI:N:a:e:v:n:o:G:s:",["help","interface","namespace","author","email","virtual_decon","name","output_dir","google_test","setup_teardown"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"         
        usage()                         
        sys.exit(2)       
    
    if len(opts) < 1 :
        usage()
        sys.exit(2)

    cpp = CppArg.CppArg()

    output = mapping_args(opts , cpp)

    dir = dir if output is None else output
    #pass
    classfile = ClassGenerator.ClassGenerator(cpp)
    if cpp.gtest:
        gtest = GoogleTestGenerator.GoogleTestGenerator(cpp)
        gtest.Build()
    #classfile.SetBaseClass(cpp.interface.pop(0))

    classfile.Build()    
    
if __name__ == "__main__":
    main(sys.argv[1:])