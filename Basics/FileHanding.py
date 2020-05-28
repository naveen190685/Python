#Open a file in read only mode
# mode:
#   r = readonly mode
#   w = write mode
myFile = "C:/Users/navkumar16/PycharmProjects/Practise/Programs/Basics/Resources/myFile.txt"
handle = open(myFile, 'r')

# #Printing each line
# for line in handle:
#     print(line)

#Reading everything in a single string
content = handle.read()
print(content)
print(f'Handle mode: {handle.mode}')

#Below code again execute read on the file handle 'handle'
content1 = handle.read()
#Below code will be an empty string, reason being the file handle 'handle' was already at file end
#hence it has nothing to read
print(content1)
#
#Searching line starting with "From: "
From = ""
for line in open(myFile, 'r'):
    if line.startswith("From: "):
        From = From + line
#
print("**************** PRINTING ALL LINES WITH FROM ********************")
print(From)
#
# #Counting the lines as per a criteria: Subject:
count, subjects = 0, ""
for line in open(myFile, 'r'):
    if line.startswith("Subject: "):
        count = count+1
        subjects = subjects + line
print("************* SUBJECTS")
print(subjects)
print(f'Total Subjects: {count}')

handle.close()

# You can use with block for handling a file and you don't need to close the handle later
def countWordsInFile(path):
    try:
        with open(path) as f:
            s = ""
            count = 0
            for line in f:
                # count = count + len(line.split())
                for n in line.split():
                    count = count + len(n)
            return count
    except FileNotFoundError:
        return -1

print(f'The total words in the file are: {countWordsInFile("sdlfkj")}')

print("*********** READ LINE BY LINE ***********")
handle = open(myFile, 'r')
print('Reading lines all at once and store each line in list using handle.readlines()')
print('\tlistOfLines = handle.readlines()')
listOfLines = handle.readlines()
print(f'listOfLines = {listOfLines}')

print('Reading single line at one time with handle.readline()')
handle = open(myFile, 'r')
print(f'Line 1: {handle.readline()}')
print(f'Line 2: {handle.readline()}')


