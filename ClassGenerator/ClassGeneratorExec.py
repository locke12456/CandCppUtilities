import ClassGenerator
import CppArg
import getopt
import sys
import argparse
import os

def usage():
    parser = argparse.ArgumentParser()

    parser.add_argument('-I','--interface', help=' ')
    parser.add_argument('-N','--namespace', help=' ')
    parser.add_argument('-n','--name', help='class name . e.g. -n file ')
    parser.add_argument('-v','--virtual_decon', help='class has virtual deconstuctor . ')
    parser.add_argument('-o','--output_dir', help='output directory. e.g. -o path ')
    parser.print_help()
    print "usage example : python ClassGeneratorExec.py -I IMqtt -v 1 -N Mqtt -n MqttInstance "
    

def set_name(cpp,val):
    cpp.name = val

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
        if opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        if options.has_key(opt):
            options[opt](opt,arg)
    return output
def main(argv):
    dir = os.getcwd() + "\\ouput\\"

    try:                                
        opts, args = getopt.getopt(argv, "hI:N:v:n:o:",["help","interface","namespace","virtual_decon","name","output_dir"])
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

    #classfile.SetBaseClass(cpp.interface.pop(0))

    classfile.Build()    
    
if __name__ == "__main__":
    main(sys.argv[1:])