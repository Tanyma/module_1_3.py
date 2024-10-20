immutable_var = (4,9,True,'False',[1,2,3])
immutable_var[4][2] = [2,1]
print (immutable_var)
#кортеж как и список может содержать в себе все типы данных, в том числе изменяемые данные (списки, словари), но само изначальное состовляющее картежа нельзя изменить\дополнить\удалить
mutable_list = [4,9,"True","cat"]
mutable_list[2] = immutable_var[3]
print(mutable_list)