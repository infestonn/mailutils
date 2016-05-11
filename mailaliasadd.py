from shutil import copy
copy('aliases', 'aliases.old')
f = open('aliases.old', 'r')
fn = open('aliases', 'w')
input_alias = input("Enter alias: ")
name = input("Enter user to add: ")
_list = []
_str = ''
ex1 = False
ex2 = False
while input_alias == name:
    print ("Are you f*cking kiddin?")
    input_alias = input("Enter new aliass: ")
    name = input("Enter new name: ")
for _stroka in f:
    if input_alias == _stroka[:_stroka.find(":")]: #lookin for existed alias
        _list = _stroka.split(",") #make a list from string with coma devider
        _list[-1] = _list[-1].replace('\n','') #delete newline from sting
        if len(_list) == 1: #check if there's more than 1 name in alias
            _list = [input_alias+":", _list[0][len(input_alias)+1:]] #split list from 1 to 2 elements
            for g in _list[1:]:
                if g == name:
                    print ('%s already in this alias' % name)
                    ex2 = True
                else:
                    _str += g
                    _stroka = _stroka[:-1] + ',' + name + '\n' #remove \n at the and of string and adds "name"
                    print ("%s added to alias %s" % (name, input_alias))
                    ex2 = True
        else:
            _list = [input_alias+":", _list[0][len(input_alias)+1:]] + _list[1:]
            for g in _list[1:]: #check whether name already in alias
                if g == name:
                    print ('%s already in this alias' % name)
                    ex2 = True
                    ex1 = True
            if ex1 != True:
                _stroka = _stroka[:-1] + ',' + name + '\n'
                print ("%s added to alias %s" % (name, input_alias))
                ex2 = True
            else:
                _stroka = _stroka
    fn.write(_stroka)
if ex2 == False:
    if _stroka[-1] != "\n": # check if file has a newline
        _stroka = "\n" + input_alias + ":" + name + "\n" #if not - add "\n"
        print ("%s added to alias %s" % (name, input_alias))
        fn.write(_stroka)
    else: # if has
        _stroka = input_alias + ":" + name + "\n"
        print ("%s added to alias %s" % (name, input_alias))
        fn.write(_stroka)
fn.close()
f.close()
from subprocess import call
call(["newaliases"])