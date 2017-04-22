# import xml.etree.ElementTree as Et
from lxml import etree as Et
import os
import argparse
import sys

__author__ = 'MWadswo'
# User cases
# Modify option in specified configurations for one or many .ewp's
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

#######################################
# Function Defs
#######################################


# Find all setting by text value
def find_elem_by_text(text):
    found_elements = []
    for elem in root.iter():
        if elem.text == text:
            found_elements.append(elem)
    return found_elements


# Returns the text of the configuration tag an element is under, or None if N/A
def get_element_configuration(elem):
    # Check for bad param
    if elem is None:
        return None

    walk_up_elem = elem

    # Walk up tree, saving element until configuration is found
    while walk_up_elem.tag != None and walk_up_elem.tag != 'configuration':
        walk_up_elem = walk_up_elem.getparent()

    return walk_up_elem[0].text


def count_siblings(elem):
    i = 0
    for sibling in elem.itersiblings():
        i += 1
    return i

# Handling if a selected options has multiple states like CCIncludePath2
def multi_state_options(elem):
    print "multiple sibling handlings"

    i = 0
    for sibling in elem.itersiblings():
        print i, ": " + Et.tostring(sibling)
        i += 1

    # Print user selected element from sibling list
    sibling_list = list(elem.itersiblings())
    print Et.tostring(sibling_list[int(raw_input("Select element to modify: "))])

    # Select modify action (insert before, insert after, (or insert id?) delete, modify)


def makelementstoconfigdict(elem):
    elemtoconfigdict = {}
    # for elem in listelemets:
    #     elemtoconfigdict[elem] = elem


# Scan for project files. Return list.
def find_ewp_files(dir_path):
    # todo allow dir_path to be a file path
    ewp_list = []

    # If not a complete path, try joining with current working directory
    if not os.path.isdir(dir_path):
        dir_path = os.path.join(os.getcwd(), dir_path)
        if not os.path.isdir(dir_path):
            sys.exit("Provided folder is found.")

    for dirpath, dirnames, filenames in os.walk(os.path.abspath(dir_path), followlinks=True):
        for filename in [f for f in filenames if f.endswith(".ewp")]:
            # print os.path.join(dirpath, filename)
            # Create a list structure of project files
            ewp_list.append(os.path.join(dirpath, filename))

            # Present a numbered list of found project files to user to confirm for editting
            # Allow user to remove some found files by entering the relevant number
            # Allow user to finalize list
    return ewp_list


#######################################
# Script logic
#######################################
# Add arguments
# Add optional number of arguments(?) to pull in variable number of dirs/files
# If arguments include directory(ies)
# Pull directory from parameter to scan for project files
parser = argparse.ArgumentParser(
    description='Parse EWP (PEWP) is a script used to change project settings in multiple IAR .ewp files'
                ' simultaneously. Example command line call: python ParseEWPs.py "\TestEwps" "CCCompilerRuntimeInfo" Debug Release',
)

parser.add_argument('proj_root_dir', action="store", help="Upper directory containing all project files"
                                                          "you wish to modify.")
parser.add_argument('option_name', action="store", help="Option to modify.")
parser.add_argument('configs_to_update', nargs='+', help="List of project configurations to update")
parse_options = parser.parse_args()
print(parser.parse_args())

ewp_list = find_ewp_files(parse_options.proj_root_dir)  # Parse XML files into element tree

# Find specified option under specific configuration branches(tag?)
selected_config = parse_options.configs_to_update
selected_option = parse_options.option_name
#
selected_value = 'TEST'

if not ewp_list:
    sys.exit("Didn't find any .ewp files.")

for file in ewp_list:
    tree = Et.parse(file)
    root = tree.getroot()

    # Find option, if specified config, modify
    for elem in tree.iter():
        if elem.text == selected_option:
            if get_element_configuration(elem) in selected_config:
                if count_siblings(elem) == 1:
                    elem.getnext().text = selected_value
                else:
                    print 'Not a single state option. Don\'t know how to merge those' \
                          'across multiple files.'
                    break

    # Add test to file output name
    path, file_name = os.path.split(file)
    file_name = 'test' + file_name

    # todo overwrite file instead of seperate test file.
    tree.write(os.path.join(path, file_name), encoding="iso-8859-1", xml_declaration=True)
