import re
inpstr= 'hello good of good in  hai society good is for on'
out = re.match('hai',inpstr) # return pattern at starting of the line..if not found it return None
out1 = re.search('hai',inpstr) # return first occurrence in entire statement ..if not found return None
out2= re.findall('hai',inpstr) # return list of pattern ..if not found return empty list
print(out)
print(out1)
print(out2)

