calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    slovo = str(string)
    print_ = (len(slovo), slovo.upper(), slovo.lower())
    count_calls()
    return print_

def is_contains(string, list_to_search):    # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Armageddon'))
print(string_info('Capybara'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)