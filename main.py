import re
import string

var_dict = dict()


def variable_check(exp):
    def_dict = dict()
    if '=' in exp:
        eq_ind = exp.index('=')
        if not exp[:eq_ind].isalpha():
            print("Invalid identifier")
        elif not exp[eq_ind + 1:].isdigit():
            if exp[eq_ind + 1:] in var_dict.keys():
                def_dict[exp[:eq_ind]] = var_dict[exp[eq_ind + 1:]]
                var_dict.update(def_dict)
            elif not exp[eq_ind + 1:].isalpha():
                print("Invalid assignment")
            elif exp[eq_ind + 1:] not in var_dict.keys():
                print('Unknown variable')
        else:
            def_dict[exp[:eq_ind]] = exp[eq_ind + 1:]
            var_dict.update(def_dict)
        return True
    return False


if __name__ == '__main__':
    print('''Allowed commands:
    /help for info
    /dict for variables info
    /exit to leave\n''')
    while True:
        a = (' '.join(input('Expression: ').split())).replace(' ', '')
        if not a:
            continue
        elif a == '/exit':
            print('Bye!')
            break
        elif a == '/help':
            print('The program calculates the sum of numbers')
        elif a == '/dict':
            print(var_dict)
        elif a.startswith('/'):
            print('Unknown command')
        elif variable_check(a):
            pass
        else:
            if not re.match(r".*[*+-/^()].*", a):
                try:
                    print(var_dict[a])
                except KeyError:
                    print('Unknown variable')
            else:
                expression = str()
                for i in a:
                    if i not in string.punctuation and i.isalpha():
                        expression += var_dict[i]
                    else:
                        expression += i
                try:
                    if not re.match(r".*//.*", a):
                        print(eval(expression.replace('^', '**')))
                    else:
                        raise SyntaxError
                except (SyntaxError, NameError) as e:
                    print('Invalid expression')
