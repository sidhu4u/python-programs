from strfun import reverse, charremove, substring, padding, remove_punctuations, count_duplicate, string_found


def pgm1():
    s = input("Enter String :")
    if s == reverse(s):
        return f"String '{s}' is Palindrome."
    else:
        return f"String '{s}' is Not Palindrome."


def pgm2():
    s = input("Enter String :")
    return f'Reverse String = "{reverse(s)}"'


def pgm3():
    s = input("Enter String :")
    c = input("Enter removing Character : ")
    return f"after removing character '{c}' = '{charremove(s, c)}'"


def pgm4():
    s = input("Enter String :")
    subs = input("Enter Substring : ")
    sub = substring(s, subs)
    if sub[0]:
        return f"substring '{subs}' present {sub[1]} times in Given string."


def pgm5():
    s = input("Enter String or word :")
    sym = input("Enter symbol to padd left and right : ")
    size = int(input("Enter size (in numbers) : "))
    return padding(s, size, sym)


def pgm6():
    s = input("Enter String or word :")
    return f"After removing punctuations marks words :\n{remove_punctuations(s)}"


def pgm7():
    s = input("Enter String or word :")
    res = count_duplicate(s)
    out = ''
    print("Each character count :")
    for i in range(len(res[0])):
        out += f"{res[0][i]} = {res[1][i]} , "
    return out


def pgm8():
    s = input("Enter String or word :")
    return f"--------------------------\n\
'{s}' found at count {string_found(s)}\n\
--------------------------"


def invalid():
    return "Invalid Choice!"


question_choice = {
    '1': pgm1,
    '2': pgm2,
    '3': pgm3,
    '4': pgm4,
    '5': pgm5,
    '6': pgm6,
    '7': pgm7,
    '8': pgm8
}


def choices(choice):
    return question_choice.get(choice, invalid)()
