__author__ = 'MWadswo'

# Parse XML files into element tree
ewp_ = os.path.join(dir_path + '\\S3_Test.ewp')
tree = Et.parse(ewp_)
root = tree.getroot()


# def testselfbindlist(list):
#     print "Function in list", list
#     list = list
#     list.append("five")
#     print "Modified list", list
#
# def testrebind
#
# thislist = ["one","two"]
# testselfbindlist(thislist)
# print "outside", thislist

# import string
# trans = string.maketrans('QnLM1Jq9i3oGkIFSX4?drCBYWObygftl8xzKD5wAsNUTR6ZjphHc', string.ascii_letters)
# text = '6ik1 WFr 1I3FW BQ?diIq i? IFd BQ?d1M'
# print text.translate(trans)

# Test
print root[1][0].text

# Prompt user for an XML tag to change

# For each   project
    # Find specified xml tag
    # Present relevant(?) tree structure to user (Ex: S128 Test - Debug -> Linker Settings -> Disable exceptions)
    # Allow user to white/black list options for editing
    # Prompt for new tag value
    # Edit Tag value
# for elem in root.iter('name'):
#     if elem.text == 'CCIncludePath2':
#         option == elem
#         include_path = elem.findall('state')
#         print include_path
# Syntax: tag
print tree.findall(".//configuration")
# Syntax: [tag]
print tree.findall(".[configuration]")
# Syntax: [tag='text']
print tree.findall("[name='CCIncludePath2']")

#####################
# XML
#####################

# Pulled from stackoverflow. Print absolute path of entire tree
def print_abs_path(root, path=None):
    if path is None:
        path = [root.tag]

    for child in root:
        if child.text is not None:
            text = child.text.strip()
        else:
            text = 'None'

        new_path = path[:]
        new_path.append(child.tag)
        if text:
            print '/{0}, {1}'.format('/'.join(new_path), text)
        print_abs_path(child, new_path)


configuration_elements = tree.findall(".//configuration")
for elem in configuration_elements:
    config_elem = elem.find('name')
    if config_elem.text in selected_config:
        print 'found selected config!'
        print 'tree.findtext'
        print(tree.findtext('toolchain'))
        print config_elem.findtext('ARM')
        print list(config_elem)

# All find____ functions search by tag name or path and most don't have text!
# I think returned elements lose their tree association as well!
# Individual elements have very little information,
# I think what I want is all stored in a relative fashion within the tree

print 'Examples'
print '*' * 10
print root.findtext('name')      # Return text by tag of immediate children. Path can be used for greater depth.
print list(root)

# for elem in tree.iter('name'):
#     if elem.text == 'CCIncludePath2':
#         option = elem[.//..]
#         include_path = elem.findall('state')
#         print include_path

        # for CCIncPathElems in elem.iter():
        #     print 'state? ' + CCIncPathElems.text

# Prompt user to open compare tool (if in clearcase) for file


# def printchild(element):
#     for child in element:
#         print child.tag
#         print child.text
#         printchild(child)
# Et.dump(root)
# print root.findall('.//Option')

# Print absolute path of entire tree
# print_abs_path(root)

print 'getparent test'
print root[0].getparent()
print root[0].getparent().getparent() # Returns None


# Working config find
# for elem in tree.findall(".//configuration"):
#     print elem.find('name').text

