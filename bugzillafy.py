from bs4 import BeautifulSoup
import re
from bs4 import NavigableString
from bs4 import *
#load the file
with open("rn625.html") as infhand:
    txt = infhand.read()


soup = BeautifulSoup(txt, 'html.parser')
outfhand = open("relnotes.html", "w")
# We're looking for the <strong> tag
for tag in soup.find_all('strong'):
    # Then inside the <strong> tag, we're picking up all lines that start with "Issue...", this will leave out "Fixed Issues" because we don't need to look up the fixed ones. :)
    if re.search("^Issue", tag.contents[0]):
        try:
             bug_No = (re.findall('\\S ([0-9]+):', tag.contents[0]))
             # Now that we got the bug#, we need to replace the contents of this tag with the bugzilla query for the said bug#
             print (bug_No[0])
        except IndexError:
                  print("value error reached")
                  continue


        bugzilla_query = "<a href=https://bugzilla.eng.vmware.com/show_bug.cgi?id="+bug_No[0]+">"+bug_No[0]+"</a>"
        #trying to see what the string looks like: it's enclosed within the <strong>..</strong>
        #print ("this is how the string looks with tags:", tag)
        print (bugzilla_query)
        # so you need to search from bug_No until the </strong> tag and extract everything that's there for the second string
        new_string = str(tag)
        bugpos = new_string.find(bug_No[0])
        strongpos = new_string.find('</strong>', bugpos)
        rest_of_string = new_string[bugpos+7:strongpos]

        new_tag_contents =   "<strong>Issue "+bugzilla_query+rest_of_string+"</strong>"
        #tag = new_tag_contents <---- not working
        tag.replace_with(new_tag_contents)
        #print (tag)
        #input ('wait')

    #    new_tag_contents = soup.new_tag("<strong>Issue "+bugzilla_query+rest_of_string+"</strong>")

    #    tag.clear
    #    soup.append(new_tag_contents)

#Is changing the tag, also changing the soup????? 12/27/16
        #tag.replace_with(new_tag_contents)
        #print (soup.tag)
           #    tag.string = new_tag_contents
    #    print ("this is the new one: ",tag.string)
        #input ('wait')
    #    outfhand.write(str(soup))

infhand.close()
html = soup.prettify(soup.original_encoding)

with open("relnotes.html", "w") as outfhand:
    outfhand.write(str(soup))

input("done, check the html file")
