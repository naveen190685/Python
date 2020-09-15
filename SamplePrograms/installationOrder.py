software__dictionary = {}
softwareToInstall = []
dependencyGuide = []
install = []
cyclic, currentInput = "", ""
new = True
ErrorMessage = ""


def dependencyGuess(software: str):
    global dependencyGuide, cyclic, ErrorMessage

    if software in install:
        dependencyGuide.pop()
        return dependencyGuide

    # if the software exists in software dictionary
    if software in software__dictionary.keys():

        # if the software's dependency is not None
        if software__dictionary.get(software) is not None:

            # if the dependency is not already added
            if software__dictionary.get(software) not in dependencyGuide:

                # add dependency to software dependency list
                dependencyGuide.append(software__dictionary.get(software))

                # if the dependency exists in software dictionary
                if dependencyGuide[len(dependencyGuide) - 1] in software__dictionary.keys():

                    # call the function again to add the dependency for the dependent software just added
                    dependencyGuess(dependencyGuide[len(dependencyGuide) - 1])

            # if the dependency is already added
            else:

                # collect all the softwares before this dependency
                for li in dependencyGuide[0:-1]:
                    if cyclic == "":
                        cyclic = li + " "
                    cyclic = cyclic + software__dictionary.get(li) + " "

                # raise exception mentioning all previous added dependencies
                ErrorMessage = "INPUT: " + currentInput + " ==>  There is a cyclic dependency issue between " + cyclic
                raise Exception(ErrorMessage)


def addMore(dep=[], myLis=[]):
    for n in myLis:
        if n not in dep:
            dep.append(n)
    return dep


software__dictionary = {
    "unittest": "testdata",
    "testdata": "metapy",
    "metapy": "colorpy",
    # "metapy": "unittest",
    "colorpy": "pyruby",
    "pyfail": "colorpy",
    "pyruby": None,
    "pychecks": "colorpy",
    "pycff": "pyruby"
}

softwareToInstall = ["unittest", "pyfail"]

# loop for the asked softwares one by one
for sw in softwareToInstall:

    # store the context for current software for which you need to know dependencies
    currentInput = sw

    # clear dependency for the software to store fresh for the context
    dependencyGuide.clear()

    # if the asked software is not already in the install list
    if sw not in install:

        # add the software to the dependency list as collecting dependencies won't do it
        dependencyGuide.append(sw)

        try:
            # collect all the dependencies for the asked software
            dependencyGuess(sw)

        except:
            # print the error message if encountered any exception
            print("ERROR: " + ErrorMessage)

            # proceed to next software asked
            continue

        # collect or append the unique softwares needed
        install = addMore(install, dependencyGuide)

# print the collected dependencies for the asked softwares
print(install)
