# import xml.etree.ElementTree as Et
from lxml import etree as Et
import os
import sys

__author__ = 'MWadswo'
# User cases
# Modify option in specified configurations for one or many .ewp's
import argparse
# python MegaProjParser.py
# User gives string to search for xml tag text
# 1. Modify that value
# 2. Use getprevious/getnext to find value nearby tag to modify
#    (state/version)
# 3. Insert new element next to (adding new include path)

# Find option name.txt, modify matching state.text
# Include path
# Find option name.text based on configuration name
# Insert/delete/Modify element text of desired state.text

# Have to construct paths to access elements directly
# Because find_____ only works off of paths/tags and our tags are useless
# and i don't want to code to the project layout.
# Itertext can perform a text search, can i get the element while the iterator
# is on it though?
# Iter and in keyword will return the element So I might be able to calculate it's path?
# Can i get the path between a root and element?


parser = argparse.ArgumentParser(
    description='Example with nonoptional arguments',
)

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print(parser.parse_args())

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


# Find all setting by text value
def findelementbytext(text):
    foundelements = []
    for elem in root.iter():
        if elem.text == text:
            foundelements .append(elem)
    return foundelements

# Returns the text of the configuration tag an element is under, or None if N/A
def getelementsconfiguration(elem):
    if elem is None:
        return None

    walk_up_elem = elem

    while walk_up_elem.tag != None and walk_up_elem.tag != 'configuration':
        walk_up_elem = walk_up_elem.getparent()

    return walk_up_elem[0].text


def makelementstoconfigdict(elem):
    elemtoconfigdict = {}
    # for elem in listelemets:
    #     elemtoconfigdict[elem] = elem

dir_path = os.path.dirname(os.path.realpath(__file__))

# Add arguments
    # Add optional number of arguments(?) to pull in variable number of dirs/files
# If arguments include directory(ies)
    # Pull directory from parameter to scan for project files

# Scan for project files
ewp_list = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".ewp")]:
        # print os.path.join(dirpath, filename)
        # Create a list structure of project files
        ewp_list.append(os.path.join(dirpath, filename))

# Present a numbered list of found project files to user to confirm for editting
    # Allow user to remove some found files by entering the relevant number
    # Allow user to finalize list

# Parse XML files into element tree
ewp_ = os.path.join(dir_path + '\\S3_Test.ewp')
tree = Et.parse(ewp_)
root = tree.getroot()


# Find specified option under specific configuration branches(tag?)
selected_config = ['Release', 'Debug']
selected_option = 'CCCompilerRuntimeInfo'
selected_value = 'TEST'

# Count number of state siblings of given elem
def count_option_state(elem):
    return len(elem.getparent().findall('state'))


# Find option, if specified config, modify
for elem in tree.iter():
    if elem.text == selected_option:
        if getelementsconfiguration(elem) in selected_config:
            elem.getnext().text = selected_value

tree.write(os.path.join(dir_path, 'testout.ewp'))
