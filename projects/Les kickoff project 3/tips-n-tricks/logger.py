# Constants
LEVEL_INFO = 3
LEVEL_WARN = 2
LEVEL_ERROR = 1
LEVEL_FATAL = 0

# Default level
logLevel = LEVEL_INFO


def setLogLevel(level):

    # Because we want to change the module's logLevel
    global logLevel

    logLevel = level


def logInfo(msg):

    if logLevel >= LEVEL_INFO:

        print("INFO: ", msg)


def logWarn(msg):

    if logLevel >= LEVEL_WARN:

        print("WARN: ", msg)


def logError(msg):

    if logLevel >= LEVEL_ERROR:

        print("ERROR: ", msg)


def logFatal(msg):

    if logLevel >= LEVEL_FATAL:

        print("FATAL: ", msg)