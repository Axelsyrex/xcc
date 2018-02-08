#!/usr/bin/env python
from plistlib import readPlist, writePlist


def main():
    fileName = "/Applications/Xcode.app/Contents/Frameworks/IDEKit.framework/Versions/A/Resources/IDETextKeyBindingSet.plist"
    with open(fileName, 'r') as fp:
        textKeyBindingSetPlist = readPlist(fileName)
    customizedKey = "Customized"
    textKeyBindingSetPlist[customizedKey] = customizedDict()
    writePlist(textKeyBindingSetPlist, fileName)


def customizedDict():
    customizedDict = {
        "Move Down 5": "moveDown:, moveDown:, moveDown:, moveDown:, moveDown:",
        "Move Up 5": "moveUp:, moveUp:, moveUp:, moveUp:, moveUp:",
        "Move Left 5": "moveLeft:, moveLeft:, moveLeft:, moveLeft:, moveLeft:",
        "Move Right 5": "moveRight:, moveRight:, moveRight:, moveRight:, moveRight:"
    }
    return customizedDict


if __name__ == "__main__":
    main()
