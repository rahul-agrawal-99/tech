
import re

'''
[]	A set of characters	                                                                       "[a-m]"	

\	Signals a special sequence (can also be used to escape special characters)	              "\d"	

.	Any character (except newline character)	                                                "he..o"	

^	Starts with	                                                                              "^hello"	

$	Ends with	                                                                               "planet$"
	
*	Zero or more occurrences	                                                               "he.*o"	

+	One or more occurrences                                                                 	"he.+o"	

?	Zero or one occurrences	                                                                     "he.?o"	

{}	Exactly the specified number of occurrences                                                	"he.{2}o"	

|	Either or	                                                                               "falls|stays"	

()	Capture and group

[123] can match 1, 2 or 3 in the string.
'''
'''
Character                	Description	                                                                        Example	                
\A	            Returns a match if the specified characters are at the beginning of the string                	    "\AThe"	

\b          	Returns a match where the specified characters are at the beginning or at the end of a word         r"\bain"
                (the "r" in the beginning is making sure that the string is being treated as a "raw string")	   r"ain\b"	
                
\B	     Returns a match where the specified characters are present, but NOT at the beginning                       r"\Bain"
                (or at the end) of a word
        (the "r" in the beginning is making sure that the string is being treated as a "raw string")	           r"ain\B"	


\d	            Returns a match where the string contains digits (numbers from 0-9)	                                   "\d"	

\D	            Returns a match where the string DOES NOT contain digits	                                           "\D"	

\s	            Returns a match where the string contains a white space character	                                   "\s"	

\S	            Returns a match where the string DOES NOT contain a white space character	                            "\S"
	
\w	            Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, 
                    and the underscore _ character)	                                                                    "\w"	
                    
\W	            Returns a match where the string DOES NOT contain any word characters	                                 "\W"	

\Z	            Returns a match if the specified characters are at the end of the string	                        "Spain\Z"
'''

text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements (78) rahul@df.com 
Unaudited Interim Financial Statements (78) rahul2002@df.com 
asfThe rain in Spain.
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020. a 
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In The previous quarter i.e. FY2020 Q4 it was $3 billion
aaaaaabbb
'''


# pattern = '\(\d\d'    
# # pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'    
# # \ is used to determine every character to be indentified 
# #  e.g. \(   => only char "("  , \(\d\)  => "(" with digit and ")" => (5)
# # can be used for 2 consecutive charachters like \(-   for "(-" , cant be used for \d 

# matches = re.findall(pattern, text)

# print(matches)


# pattern = '([0-9]+)'  # get all the num. letters all at once if avilable like 2020  will be 2020
# pattern = '([0-9])'   # get each number letter seperately  like 2020 will be 2 ,0 ,2 ,0

# pattern = '([a-c]+)'   # get all having a , b ,c or acc , bc , aaaaaabbb

# pattern = 'Note \d - ([^\n]*)'    # start with "Note" followed by digit and then anything between this and new line char "\n"
# pattern = '\d{4}'   # minimum 4 consecutive digits like 2020 , 4589

pattern = '([A-Z]).*'       



# pattern = 'The.*Spain.$'        # start with "The" (^) , followed by any no . of letters and ends with "Spain." 



# pattern = '\w+'  # get every word present in text
# text = "adf rahul@rt.vi sdgf"


# pattern = '([a-z0-9)]+)@([a-z]+)\.([a-z]+)'  # get mail id in groups like  ('rahul', 'df', 'com')
# pattern = '[a-z0-9]+@[a-z]+\.[a-z]+'  # get mail id fully like rahul@df.com

# pattern = '([A-Z])([a-z]+)'  # get first letter of each word and rest of the word

# matches = re.findall(pattern, text ,flags=re.IGNORECASE  )       

# matches = re.findall(pattern, text)   #findall() function returns a list containing all matches.
# print(matches)
# matches = re.match(pattern, text)   #search() function searches the string for a match, and returns a Match object if there is a match.
                                    # If there is more than one match, only the first occurrence of the match will be returned
# print(matches)

# split = re.split("\.", text)            
# split = re.split("\s", text)            
# split() function returns a list where the string has been split at each match:
 # split based on simple blank space i.e => " "
                                        
# sub  = re.sub("\s", "9", text)        # sub() function replaces the matches with the text of your choice
                                    # here " " will be replaced with 9


# print(split)
text = "1123.456.abc.def"
pattern = '([0-9]{3}).([0-9]{3}).([a-zA-Z]+)'

match = re.match(pattern, text) is not None

print([re.match(pattern, text)])

print(str(match).lower())








