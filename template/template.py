from subprocess import call
import sys
list = sys.argv
header = list[1]+".h"
call(["touch",header])
hfile = open(header,"w")
defineHeader = list[1].upper()
hfile.write("#ifndef __"+defineHeader+"_H__                 \n")
hfile.write("#define __"+defineHeader+"_H__                 \n")
hfile.write('#include '+'"'+'semaeapi.h'+'"'+'              \n')
hfile.write('#include '+'"'+'ISEMA_EApiCommand.h'+'"'+'     \n')
hfile.write("class "+list[1]+" : public ISEMA_EApiCommand   \n")
hfile.write("{                                              \n")
hfile.write("public:                                        \n")
hfile.write("	"+list[1]+"();                               \n")
hfile.write("	~"+list[1]+"();                              \n")
hfile.write("	virtual bool Command();                      \n")

hfile.write("#if (SEMA_MQTT)                                         \n")
hfile.write("	virtual ISemaMqttPayload::Property getProperties();  \n")
hfile.write("#endif                                                  \n")

hfile.write("   virtual boost::program_options::options_description Help(); \n")
hfile.write("};                                             \n")


hfile.write("#endif                                             \n")

hfile.close()

cpp = list[1]+".cpp"
call(["touch",cpp])
cppfile = open(cpp,"w")
#include "test.h"

cppfile.writelines('#include '+'"'+header+'"'+'   \n')
cppfile.writelines(""+list[1]+"::"+list[1]+"()    \n")
cppfile.writelines("{                             \n")
cppfile.writelines("}                             \n")
cppfile.writelines("                              \n")
cppfile.writelines("                              \n")
cppfile.writelines(""+list[1]+"::~"+list[1]+"()   \n")
cppfile.writelines("{                             \n")
cppfile.writelines("}                             \n")
cppfile.writelines("                              \n")

cppfile.writelines("boost::program_options::options_description "+list[1]+"::Help()  \n")
cppfile.writelines("{                                                                \n")
cppfile.writelines("	boost::program_options::options_description help;            \n")
cppfile.writelines("    help.add_options();                                          \n")
cppfile.writelines("	return help;                                                 \n")
cppfile.writelines("}                                                                \n")
cppfile.writelines("#if (SEMA_MQTT)                                                  \n")
cppfile.writelines("ISemaMqttPayload::Property "+list[1]+"::getProperties()          \n")
cppfile.writelines("{                                                                \n")
cppfile.writelines("	ISemaMqttPayload::Property json;                             \n")
cppfile.writelines('	json['+'"'+'pBuffer'+'"'+'] = boost::any_cast<std::string>(Output[0]);\n')
cppfile.writelines("	return json;                                                 \n")
cppfile.writelines("}                                                                \n")
cppfile.writelines("#endif                                                           \n")

cppfile.writelines("bool "+list[1]+"::Command()   \n")
cppfile.writelines("{                             \n")
cppfile.writelines("	"+"uint32_t handler;      \n")
cppfile.writelines("    //bool result = "+list[2]+"(handler,      \n")
cppfile.writelines("	"+"return true;      \n")
cppfile.writelines("}                             \n")
