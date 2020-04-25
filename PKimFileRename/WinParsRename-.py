#
#
#
import shutil, os, re

#matchAlpha = re.compile("(a-z)(*.*?)$", re.IGNORECASE)

matchAlpha = re.compile(r"""^([a-zA-Z]+) # all letters before non-letters
(.*?)$ # all text after the date
""", re.VERBOSE)

# Loop over files wihin working directory
for OldFileName in os.listdir('.'):

    mo = matchAlpha.search(OldFileName)

    # Skip files without a date
    if mo == None:
        print ("Breaking out of Loop")
        print ("Cannot find a match")
        continue

    alphaBeforeHyphenPart = mo.group(1)
    afterHyphenPart = mo.group(2)

    NewFileName = alphaBeforeHyphenPart + '-' + afterHyphenPart

    # Get the full obsolute filepath
    absWorkingDir = os.path.abspath('.')
    OldFileName = os.path.join(absWorkingDir, OldFileName)
    NewFileName = os.path.join(absWorkingDir, NewFileName)

    # Rename the files.
    print(f'Renaming "{OldFileName}" to "{NewFileName}"...')
    shutil.move(OldFileName, NewFileName) # uncomment after testing
