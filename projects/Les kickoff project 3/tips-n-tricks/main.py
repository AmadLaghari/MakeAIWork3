import module
import logger
import unit

def main():
    print(module.ModuleVar)
    print(module.moduleFunc())

    # module.funcFromOtherModule()
    
    # print(module.varFromOtherModule)


if __name__ == "__main__":

    # logger.setLogLevel(logger.LEVEL_FATAL)

    # logger.logInfo("msg")

    # unit.runTests()

    main()