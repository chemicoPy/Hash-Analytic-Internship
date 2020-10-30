


ask = int(input("Enter a number:"))

addthem1=[]
counter = 1

one = [ "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
       
ten = [ "", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "] 



def numToWords(n, s): 

    str = "" 

    if (n > 19): 
        str += ten[n // 10] + one[n % 10]

    else: 
        str += one[n]

    if (n): 
        str += s  

    return str 



def convertToWords(n): 

    out = "" 
 
    out += numToWords(((n // 1000) % 100), "thousand ") 

    out += numToWords(((n // 100) % 10), "hundred ") 

    if (n > 100 and n % 100): 

        out += "and " 
 
    out += numToWords((n % 100), "")
  

    return out


while ask < 10001:
    for j in range(2, ask):

            addthem1.append((convertToWords(counter)))

            addthem2 = ''.join(set(addthem1))



    counter = counter+1

    if counter==ask+1:
        break

print(addthem2)
print('Sum of the length of digits in words = ',len(str(addthem2).replace(" ",'')))









































