from django.template.defaultfilters import upper
from soupsieve.util import lower

calls = 0
def count_calls():
    global calls
    calls +=1

def string_info(a):
    count_calls()
    print (len(a), lower(a), upper(a))

def is_contains(string ,list_to_search):
    count_calls()
    print(str.lower(string) in (item.lower() for item in list_to_search))

is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
string_info('Armageddon')
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
