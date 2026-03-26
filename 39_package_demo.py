from googletrans import Translator
#create object
tran = Translator()
def english_to_gujarati(*line):
    global tran 
    list = []
    for word in line:
        result = tran.translate(word, src='en', dest='hi')
        # print(result.text)
        list.append(result.text)
    return list 
list = english_to_gujarati("car","books","address","name","village","tiger")
print(list)
