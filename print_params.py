def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

values_list = [[15,20,25], True, 'False']
values_list2 = [(44,"44"), 'True']
values_dict = {'a' : 45, 'b' : '123', 'c' : [True, False]}
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2,5)
print_params(5,*values_list2)

def print_dict(**kwargs):
    print(kwargs)
values_dict = {'a' : 45, 'b' : '123', 'c' : [True, False]}
print_dict(**values_dict)
