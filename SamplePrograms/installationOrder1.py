software__dictionary = {}
softwareToInstall = []
dependencyGuide = []
localDependency = []
cyclic, currentInput = "", ""
new = True
ErrorMessage = ""

software__dictionary = {
    "unittest": "testdata",
    "testdata": "metapy",
    # "metapy": "colorpy",
    "metapy": "unittest",
    "colorpy": "pyruby",
    "pyfail": "colorpy",
    "pyruby": None,
    "pychecks": "colorpy",
    "pycff": "pyruby"
}

softwareToInstall = ["unittest", "pyfail"]
allDependencies = []
for software in softwareToInstall:
    cyclic = False
    if software not in localDependency:
        localDependency.append(software)
    while software__dictionary.get(software) is not None \
            and software__dictionary.get(software) not in localDependency \
            and software__dictionary.get(software) not in allDependencies:
        localDependency.append(software__dictionary.get(software))
        software = software__dictionary.get(software)
    allDependencies = allDependencies + localDependency
    try:
        if software__dictionary.get(software) is not None and software__dictionary.get(software) in localDependency:
            ErrorMessage = str(localDependency)
            localDependency.clear()
            # print("ERROR: Cyclic depencendy " + st)
            raise Exception("Cyclic depencendy " + st)
    except:
        print("Cyclic depencendy " + ErrorMessage)
    finally:
        continue
    localDependency.clear()

# print the collected dependencies for the asked softwares
print(allDependencies)