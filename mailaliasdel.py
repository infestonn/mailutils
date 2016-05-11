from shutil import copy
copy('aliases', 'aliases.old')
f = open('aliases.old', 'r')
fn = open('aliases', 'w')
input_alias = input("Enter alias: ")
name = input("Enter user to delete: ")
t = input_alias
_list = []
_str = ''
ex1 = False
ex2 = False
for _stroka in f:
    if input_alias == _stroka[:_stroka.find(":")]: #lookin for existed alias
        ex2 = True
        _list = _stroka.split(",")
        _list[-1] = _list[-1].replace('\n','') #delete newline from sting
        _list = [input_alias+":", _list[0][len(input_alias)+1:]] + _list[1:]
        for g in _list[1:]:
            if g == name:
                print ('Deleting user \"%s\" from alias \"%s\"' % (name, input_alias))
                _list.pop(_list.index(g))
                _stroka = input_alias + ":" + ",".join(_list[1:]) + "\n"
                ex1 = True
                if len(_list) == 1:
                    _stroka = ""
                    print ("This is the last user in alias. Deleting alias \"%s\" " % (input_alias))
        if ex1 == False:
            print("There is no \"%s\" in this alias" % name)
    fn.write(_stroka)
if ex2 == False:
    print("There is no alias %s" % input_alias)
fn.close()
f.close()
from subprocess import call
call(["newaliases"])