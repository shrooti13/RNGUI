from bs4 import BeautifulSoup
import re
from bs4 import NavigableString
from bs4 import *
#load the file
with open("relnotes.html") as fhand:
    txt = fhand.read()


soup = BeautifulSoup(txt, 'html.parser')
#print(soup.prettify())
#print(soup.find_all('b'))
# We're looking for the <strong> tag
for tag in soup.find_all('strong'):
# Then inside the <strong> tag, we're picking up all lines that start with "Issue...", this will leave out "Fixed Issues" because we don't need to look up the fixed ones. :)
    if re.search("^Issue", tag.contents[0]):
#Once we have all "Issue + bug#" lines, we extract out the bug# using
#\\S = matches whitespace characters -- we don't want those, but we need them to find the numbers
# = a single space after that --- what's that for?
# () = this tells re.findall to extact only the stuff that's in the parantheses
#[0-9] = matches any digits
#+ = continues to match digits and includes all of them into the extracted string
# : = stops at the colon sign

    #    print (re.findall('\\S ([0-9]+):', tag.contents[0]))

# I need to convert the bug# extracted into a number and found this that works: http://stackoverflow.com/questions/23375606/converting-list-items-from-string-to-intpython
#        bug_No = list(map(int,(re.findall('\\S ([0-9]+):', tag.contents[0]))))
#OK, there's no need to conver bug_No into a number, because we're not doing any operation on it, just attaching to the bugzilla query so string is what we really need! duh!
        bug_No = (re.findall('\\S ([0-9]+):', tag.contents[0]))
        print (bug_No[0])
    #    input("press a key")
    #    print (tag.contents[0])

# Now that we got the bug#, we need to replace the contents of this tag with the bugzilla query for the said bug#
# we need EVERYTHING in the string, except the bug# that needs to be the new bugzilla query
        bugzilla_query = "https://bugzilla.eng.vmware.com/show_bug.cgi?id="+bug_No[0]
        input("here's the bugzilla query:")
        print (bugzilla_query)
#OK, now we have the bugzilla_query, time to replace the original string with this new addition

#       so pull out everything that occurs AFTER the bugzilla query:
#        
        new_issue_string = "Issue" + bugzilla_query +
        tag.string = ""
