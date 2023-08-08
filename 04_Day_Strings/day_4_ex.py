'''
💻 Exercises - Day 4
🌕 You are an extraordinary person and you have a remarkable potential. 
You have just completed day 4 challenges 
and you are four steps a head in to your way to greatness. 
Now do some exercises for your brain and muscles.

'''
# # 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# # method1
# list_group = ['Thirty', 'Days', 'Of', 'Python']
# STR_GROUP = list_group[0]+' '+list_group[1]+' '+list_group[2]+' '+list_group[3]
# print(STR_GROUP)
# # method2
# list_group = ['Thirty', 'Days', 'Of', 'Python']
# STR_G = ''
# for x in (list_group):
#     STR_G += x + ' '
# STR_G = STR_G.strip()
# print(STR_G)

# # 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# # method 1
# list_code = ['Coding', 'For', 'All']
# STR_CODE = list_code[0]+' '+list_code[1]+' '+list_code[2]
# print(STR_CODE)
# print(len(STR_CODE))
# # method 2
# list_code = ['Coding', 'For', 'All']
# STR_CODE = ''
# for x in list_code:
#     STR_CODE += x + ' '
# print(STR_CODE)
# print(len(STR_CODE))
# print(STR_CODE.strip())
# print(len(STR_CODE.strip()))

# # 3. Declare a variable named company and assign it to an initial value "Coding For All".
COMPANY = 'Coding For All'
# # 4. Print the variable company using _print()_.
# print('输出变量COMPANY: ',COMPANY)

# # 5. Print the length of the company string using _len()_ method and _print()_.
# print('输出变量COMPANY的长度: ',len(COMPANY))

# # 6. Change all the characters to uppercase letters using _upper()_ method.
# print('将变量COMPANY全部大写: ',COMPANY.upper())

# # 7. Change all the characters to lowercase letters using _lower()_ method.
# print('将变量COMPANY全部小写: ',COMPANY.lower())

# # 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
# print('将变量COMPANY首单词首字母大写: ',COMPANY.capitalize())
# print('将变量COMPANY转成标题: ',COMPANY.title())
# print('将变量COMPANY首字母小写: ',COMPANY.swapcase())

# # 9. Cut(slice) out the first word of _Coding For All_ string.
# print(COMPANY[0:6])

# # 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
# WORD = 'Coding'
# print(COMPANY.index(WORD))
# print(COMPANY.find(WORD))
# # 11. Replace the word coding in the string 'Coding For All' to Python.
# print('将',COMPANY,'中的coding替换成playing,结果是这样： ',COMPANY.replace('Coding','Playing'))

# # 12. Change Python for Everyone to Python for All using the replace method or other methods.
CHANGE1 = 'Python for Everyone'
# print('将',CHANGE1,'中的Everyone替换成All,结果是这样： ',CHANGE1.replace('Everyone','All'))

# # 13. Split the string 'Coding For All' using space as the separator (split()) .
# print('分词；将',COMPANY,'按照空格隔开,结果是这样： ','Coding For All'.split())
# # 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# SPLITWORD ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print('分词；将',SPLITWORD,'按照逗号隔开,结果是这样： ',SPLITWORD.split(','))
# # 15. What is the character at index 0 in the string _Coding For All_.
# print('打印',COMPANY,'第0个索引,结果是这样： ',COMPANY[0])
# # 16. What is the last index of the string _Coding For All_.
# print('打印',COMPANY,'最后的索引,结果是这样： ',COMPANY[-1])

# # 17. What character is at index 10 in "Coding For All" string.
# print('打印',COMPANY,'第10个索引,结果是这样： ',COMPANY[10])
# # 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
# # method 1
# CHANGE1 = CHANGE1.upper().split()
# print(CHANGE1)
# word0 = CHANGE1[0][0]
# word1 = CHANGE1[1][0]
# word2 = CHANGE1[2][0]
# print(f"Method1's result: {word0+word1+word2}")
# # method 2
# print(f"Method2's result: {CHANGE1[0][0]+CHANGE1[1][0]+CHANGE1[2][0]}")
# # method3
# STR_C = ''
# for x in CHANGE1:
#     STR_C += x[0]
# print(f"Mehtod3's result: {STR_C}")
# # 19. Create an acronym or an abbreviation for the name 'Coding For All'.
# #Method1
# print("************Method1 START************")
# SURPWORD ='Coding For All'
# SURPWORD = SURPWORD.upper()
# print(SURPWORD)
# print(SURPWORD.split())
# WORD0 = SURPWORD.split()[0][0]
# WORD1 = SURPWORD.split()[1][0]
# WORD2 = SURPWORD.split()[2][0]
# print(f"Method1's reslut: {SURPWORD} short for  {WORD0+WORD1+WORD2}")
# print("************Method1 END************")
# print("***********************************")
# #Method2
# print("***********Method2 START***********")
# SURPWORD ='Coding For All'
# SURPWORD = SURPWORD.upper()
# print(f"Method2's reslut: {SURPWORD} short for  {SURPWORD[0]+SURPWORD[-7]+SURPWORD[-3]}")
# print("***********Method2 END***********")

# #Method3
# print("***********Method3 START***********")
# SURPWORD ='Coding For All'
# SURPWORD = SURPWORD.upper().split() #先大写再分词成字符串
# STR_TMP = ''
# for x in SURPWORD:
#     STR_TMP += x[0]
# print(f"Method3's reslut: {STR_TMP}")

# print("***********Method3 END***********")

# # 20. Use index to determine the position of the first occurrence of C in Coding For All.
# # 21. Use index to determine the position of the first occurrence of F in Coding For All.
# # 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# # 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# # 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# SUPERWORD1='Coding For All'
# SUPERWORD2='Coding For All People'
# SUPERWORD3='You cannot end a sentence with because because because is a conjunction'
# LOOKINFOR1 = 'C'
# LOOKINFOR2 = 'F'
# LOOKINFOR3 = 'l'
# LOOKINFOR4 = 'because'
# print(f"No.20's result: {SUPERWORD1.index(LOOKINFOR1)}")
# print(f"No.21's result: {SUPERWORD1.index(LOOKINFOR2)}")
# print(f"No.22's result: {SUPERWORD2.rindex(LOOKINFOR3)}")
# print(f"No.23's result: {SUPERWORD3.index(LOOKINFOR4)}")
# print(f"No.24's result: {SUPERWORD3.rindex(LOOKINFOR4)}")

# # 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# # 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# # 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# SUPERWORD4='You cannot end a sentence with because because because is a conjunction'
# LOOKINFOR5='because because because'
# LOOKINFOR6='because'
# # 找到开始和结束的index
# STARTINDEX = SUPERWORD4.index(LOOKINFOR5)
# ENDINDEX = STARTINDEX +len(LOOKINFOR5)
# LF6STINDEX =SUPERWORD4.index(LOOKINFOR6)
# LF6ENDINDEX =LF6STINDEX+len(LOOKINFOR6)
# #使用[]直接输出
# print(f"No.25's result: {SUPERWORD4[STARTINDEX:ENDINDEX]}")
# print(f"No.26's result: {LF6STINDEX}")
# SUPERWORD4 = SUPERWORD4.replace(LOOKINFOR5,'')
# print(f"No.27's result: {SUPERWORD4}")



# 28. Does '\'Coding For All' start with a substring _Coding_?
print('\'Coding For All')
# 29. Does 'Coding For All' end with a substring coding?

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
DEALWORDS ='   Coding For All      '
print(len(DEALWORDS))
DEALWORDS =DEALWORDS.strip()
print(DEALWORDS)
print(len(DEALWORDS))

# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.