# You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.
# You have to toggle case of each character of string A.
# For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.

# Input 1: A = "Hello"
# Output 1:hELLO
def toggleCase(string):
    toggle=""
    for i in range(len(string)):
        #string[i]=ord(string[i])
        if ord(string[i])>=65 and ord(string[i])<=90:
            toggle+=(chr(ord(string[i])+32))
        elif ord(string[i])>=97 and ord(string[i])<=122:
            toggle+=(chr(ord(string[i])-32))
    return toggle
string=input()
print(toggleCase(string))