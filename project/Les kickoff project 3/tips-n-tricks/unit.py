import vat
import logger

def testVAT():

    if vat.incluceVAT(100) != 120:

        logger.logFatal("incluceVAT test failed")
    
    if vat.extractVAT(120) != 20:

        logger.logFatal("extractVAT test failed")


def runTests():

    testVAT()