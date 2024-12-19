# This course reffers as a general theme to the dictionaries in Python.
# Dictionaries represent a way of data storage.
# In essence they are a collection of data and they can be identified by unique unrepetitive keys
# Data and keys can be of any type so that make from dictionaries a great choice for data handling and manipulation
# They are very permissive but not as straightforward as other ways to keep track of data

# 1. Frequency counter
# Given a list of numbers of whatever type. Create a dictionary that stores the numbers as keys
# and frequency of appearance as values

def Frequency_Counter( inputList ):
    myDictionary = {}
    # to store data in a dictionary you should call the dictionary as the same as an array dictionary[index]
    for element in inputList:
        if element not in myDictionary:
            myDictionary[element] = 1 # first occurrence
        else:
            myDictionary[element] += 1 # multiple occurrences
    return myDictionary
# call to print the result
#print( Frequency_Counter([1,2,1,3,2,2,2,2,4,5,5,6,4,3,3,1,1,1,12,10,12,11,6,7]))
# you can sort the dictionary for the output to look better using lambda function
sortedMyDict = dict( sorted( Frequency_Counter( [1,2,1,3,2,2,2,2,4,5,5,6,4,3,3,1,1,1,12,10,12,11,6,7] ) . items() , key=lambda x:x[0] ) )
#print( sortedMyDict )



# 2. Merging 2 Dictionaries with summation. Write a function that merges 2 dictionaries and if
# there are common keys summ the components. Assume that the dictionary is filled with integer values
# the keys can be whatever: integers , strings etc
def Merge_With_Summation( dict1 , dict2 ):
    mergedDict = dict1 . copy()
    for key , value in dict2.items():
        if key in mergedDict:
            mergedDict[key] += value
        else:
            mergedDict[key] = value

    return mergedDict

#print( Merge_With_Summation({'a': 10, 'b': 20, 'c': 30} , {'b': 5, 'c': 15, 'd': 25} ) )


# 3 . Nested Dictionaries. Giving a dictionary with a nested structure. At certain keys there can be
# successive dictionaries with keys that have again dictionaries assigend and so on. And a list of access.
# Making use of them find the value at the end of the nesting structure
def Get_Value_In_Nested_Dictionary( dict , list ):
    currentDictOrValue = dict
    try:
        for key in list:
            currentDictOrValue = currentDictOrValue[key]
        return currentDictOrValue
    except (KeyError , TypeError):
        return None # no value is stored
'''
nested_dict = {'a': {'b': {'c': 42}}}
keys_to_access = ['a', 'b', 'c']
result = Get_Value_In_Nested_Dictionary(nested_dict, keys_to_access)
print(f"Value at keys {keys_to_access}: {result}")
'''

# 4. Word Frequency in a phrase. Giving an input phrase. Determine which word
# is used the most. Take into account that the phrase can have punctuation, i.e.
# standard punctuation involves . , : ; ! ?
import re
def Most_Frequent_Word( phrase , separators ):
    pattern = "|".join(map(re.escape, separators) )
    substrings = re . split( pattern , phrase )
    # split the sustrings into individual words
    words = [word for substring in substrings for word in substring.split()]
    # now words is a list of the words inside the phrase
    # in the order of their appearance
    # dictionary initialization ----> words are keys and values are their no of appearances
    myDict = {}
    # don't take into account capital letter ----> lower everything
    for word in words:
        word = word . lower()
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] += 1
    mostFword = max(myDict , key = lambda k: myDict[k])
    print( f"The most frequent word is: {mostFword}. It appears: {myDict[mostFword]} times" )

#Most_Frequent_Word( "Hello world! This is python, this is a code for dictionaries. This runs ok!" , [" ",".",",","!","?"] )


# 5. Checking Anagrams. Given two strings. Check if they are anagrams or not
# Return: They are anagrams!
#         They are not anagrams!
def Anagrams( string1 , string2 ):
    copyS1 = string1
    copyS2 = string2
    string1 = string1 . lower()
    string2 = string2 . lower()
    myDict1 = {}
    myDict2 = {}
    for letter in string1:
        if letter not in myDict1:
            myDict1[letter] = 1
        else:
            myDict1[letter] += 1
    for letter in string2:
        if letter not in myDict2:
            myDict2[letter] = 1
        else:
            myDict2[letter] += 1
    anagrams = True
    for key , value in myDict1.items():
        try:
            if myDict1[key] == myDict2[key]:
                pass
            else:
                anagrams = False
                break
        except (ValueError , KeyError):
            anagrams = False
    if anagrams:
        return f"{copyS1} and {copyS2}. They are anagrams!"
    else:
        return f"{copyS1} and {copyS2}. They are not anagrams!"

#print(Anagrams( "Lupul" , "Lulup" ))


# 6. Below threshold removal. Implement a function that gets a dictionary
# and a certain threshold value. Remove the elements that have the values below
# the threshold thus shorten the dicitonary
def Below_Threshold_Remvoval( dict , thresholdVal ):
    keysList = list(dict.keys())
    for key in keysList:
        if dict[key] < thresholdVal:
            dict . pop( key )
        else:
            pass

    return f"After removing values under {thresholdVal} -> {dict}"

#print( Below_Threshold_Remvoval({'a': 10, 'b': 5, 'c': 20, 'd': 15} , 10 ) )


# 7. Sorting a dictionary ascending or descending
def Sorting( myDict , order ):
    if order == "ascending":
        sortedItems = sorted( myDict.items() , key = lambda  x:x[1] )
        sortedDict = dict( sortedItems )
        return sortedDict
    else:
        sortedItems = sorted( myDict.items(), key=lambda x: x[1], reverse=True )
        sortedDict = dict( sortedItems )
        return sortedDict

#print( Sorting( {'key_0': 32, 'key_1': 75, 'key_2': 46, 'key_3': 91, 'key_4': 19, 'key_5': 54, 'key_6': 67, 'key_7': 10, 'key_8': 88, 'key_9': 42} , "ascending" ) )



# 8. Dictionary inversion. Create a function named Inversion that inverts the
# keys and the values of a dictionary. Basically making the values the new keys
# and the keys the new values
def Inversion( dictionary ):
    inverted_dictionary = { value : key for key , value in dictionary . items() }
    return inverted_dictionary
#print( Inversion({'key_0': 32, 'key_1': 75, 'key_2': 46, 'key_3': 91, 'key_4': 19, 'key_5': 54, 'key_6': 67, 'key_7': 10, 'key_8': 88, 'key_9': 42}) )



# 9. Common elements. Write a function Common that determines and returns the
# common elements of two dicitonaries( both keys and values ). At least one pair
# of identical keys and values is sufficient, more is even better. For example 3
# of a kind or 4 of a kind and so on
def Common( dictionary1 , dictionary2 ):
    listOfkeys = []
    listOfValues = []
    for key1 , value1 in dictionary1 . items():
        for key2 , value2 in dictionary2 . items():
            if key1 == key2 and key1 not in listOfkeys:
                listOfkeys . append( key1 )
            if value1 == value2 and value1 not in listOfValues:
                listOfValues . append( value1 )
    return f"Common keys are: {listOfkeys} and common values are: {listOfValues}"

#print( Common( {'common_key_0': 48, 'common_key_1': 72, 'common_key_2': 35, 'dict1_key_0': 9, 'dict1_key_1': 83} ,
 #              {'common_key_0': 48, 'common_key_1': 72, 'common_key_2': 35, 'dict2_key_0': 55, 'dict2_key_1': 12} ) )



# 10 . Dictionary Intersection. Given 2 dictionaries return the common keys and their asociated values
# The function will be called Intersection and will get 2 dictionaries. Function
# will return the result as instructed before, a new dictionary basically
def Intersection( dictionary1 , dictionary2 ):
    result = {}
    if len( dictionary1 ) > len( dictionary2 ):
        # iterate over the smaller dictionary, the difference in terms is not common anyways
        # keyError still has to be implemented
        for key , value in dictionary2 . items():
            try:
                if key in dictionary1:  # checking same key value from the other dictioanry
                    result[key] = ( dictionary1[key] , value ) # store the intersection values as tuples for one individual key
                else:
                    pass
            except (KeyError , ValueError):
                pass
    else:
        for key , value in dictionary1 . items():
            try:
                if key in dictionary2:
                    result[key] = ( value , dictionary2[key] )
                else:
                    pass
            except( KeyError , ValueError ):
                pass
    return f"Intersection of:\n{dictionary1}\nand\n{dictionary2}\nis:\n{result}"

#print( Intersection({'common_key_0': 42, 'common_key_1': 79, 'common_key_2': 18, 'dict1_key_0': 55, 'dict1_key_1': 20} , {'common_key_0': 91, 'common_key_1': 30, 'common_key_2': 62, 'dict2_key_0': 2, 'dict2_key_1': 73, 'dict2_key_2': 99} ))
