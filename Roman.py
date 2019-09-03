man ={1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
 # adding dictionary

def convert_into_roman(roman):
# Defining a fucntion and parameter called roman

    user=int(input("enter the number to convert it into roman="))
    if user in roman:
        return roman[user]
#if the number is in the dictionary
    else:
        roman_string=""
        for i in roman:
            for b in roman:
                if user!=0:
                    if b<user or b==user:
                        user=user-b
                        roman_string+= roman[b]
                        break
        return roman_string
#if the number is not in the dictionary


print(convert_into_roman(man))
# printing this function and parameter called man
