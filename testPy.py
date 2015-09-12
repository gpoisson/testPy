__author__ = 'GBP'


'''**********************

    TESTPY USAGE

    $: python testPy.py <program name> <testCases>


**********************'''


import sys
import os

programName = None
testCases = None


def getArgs():
    global programName
    global testCases

    if (len(sys.argv) == 1):
        programName = "echo"
        testCases = open("testCases.txt", 'r')
        '''
        print("Program name must be user-defined.\n")
        quit()
    '''
    elif (len(sys.argv) == 2):
        programName = "{}".format(sys.argv[1])
        testCases = open("testCases.txt", 'r')

    elif (len(sys.argv) == 3):
        programName = "{}".format(sys.argv[1])
        testCases = "{}".format(sys.argv[2])

    else:
        print("Wat")
        quit()


def getTestCases():
    global testCases

    tcs = []

    for line in testCases:
        tcs.append("{}".format(line))

    return tcs


def runTests():
    global programName, testCases
    for tc in testCases:
        os.system("{} {}".format(programName, tc))

def main():
    global testCases
    
    getArgs()
    testCases = getTestCases()
    runTests()

main()