import urllib2
import re

base_url = "http://www.tdcj.state.tx.us/death_row/"
main_page = "dr_executed_offenders.html"
last_statement_page = "dr_info/"

page = urllib2.urlopen(base_url + main_page).read()

reg = re.compile("dr_info/.+last.html")

strarray = []
while (reg.search(page) != None):
    location = reg.search(page)
    strarray.append(page[location.start():location.end()])
    page = page[location.end():]

for url_link in strarray[:1]: # for testing purposes, we are just going to work with one url
    page = urllib2.urlopen(base_url + last_statement_page + url_link)
    start = page.find("Last Statement:")
    end = page.find("<!-- InstanceEndEditable -->", start)
    statements = statement_split(cleanup(page[start:end]))
    #sentiment analysis

def cleanup(cleanup_string):
    #regex replaces and stuff
    #this will remove all html tags and newlines and stuff
    return cleanup_string

def statement_split(statement_string):
    #returns array of written and spoken statements
    # TODO - should work but needs to be tested
    arr = []

    if (statement_string.find("(Written statement)") != -1):
        start = statement_string.find("(Written statement)")
        arr.append(statement_string[start + len("(Written statement)")])

    if (statement_string.find("(Spoken statement)") != -1):
        start = statement_string.find("(Spoken statement)")
        arr.append(statement_string[start + len("(Spoken statement)")])

    if (arr == []):
        arr.append(statement_string)

    return arr
