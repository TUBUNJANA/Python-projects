numWords = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}
    
numberList =[1000000000,1000000,1000,100,1]

def createStringFromNum(number,rangeTypeDevisor):
    print("Num = ",number)
    if number==None:
        return ""
    string = ""
    if number//100:
        val = number//100
        number = number%100
        string += " "+numWords[val]+" "+ numWords[100]+ ' '
        
    if number:
        if numWords.get(number,False):
            string += numWords[number]+" "
        else:
            val = number%10
            number = (number//10)*10
            # print(number)
            # print(val)
            string += numWords[number]+" "+numWords[val]+" "
            
    if rangeTypeDevisor !=1:
        string += numWords[rangeTypeDevisor]+" "
        
    return string


def convertString(number):
    # print("Num = ",number)
    if number==0:
        return ""
        
    ans = ""
    reminder = None
    rangeTypeDevisor  = 1
    reminder = None
    for rangeType in numberList:
        if number//rangeType:
            if rangeType==1:
                reminder = (number // rangeType)
                number = 0
            else:
                reminder = (number // rangeType)
                number = number%rangeType
            rangeTypeDevisor = rangeType
            break
    ans += createStringFromNum(reminder,rangeTypeDevisor) + convertString(number)
    return ans
    
print(convertString(65732007))
