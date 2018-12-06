import os

rootDir = "./prank"


#for dir_, _, files in os.walk(rootDir):
#    for fileName in files:
#        relDir = os.path.relpath(dir_, rootDir)
#        relFile = os.path.join(relDir, fileName)
#        fileSet.add(relFile)
#print (fileSet)
       
for filename in os.listdir("./prank"):
    if filename[0].isdigit():
        relFile = os.path.join(rootDir, filename)
        size=len(filename[0:])
        i=0
        
        while i<size: 
           if ord(filename[i])>57:
               relFile2 = os.path.join(rootDir, filename[i:])               
               print(relFile)
               print(relFile2)
               os.rename(relFile,relFile2[0:])
               break 
           i+=1
