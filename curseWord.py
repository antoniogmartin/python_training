import urllib.request as connection

def textRead():
    quotes=open ("/Users/antonioguzman/Desktop/python/text.txt","r")
    content=quotes.read() #le encargo al objeto creado por open que lea
    quotes.close()
    checkProfanity(content)

def checkProfanity(content):
   s="http://www.wdylike.appspot.com/?q="+content
   print(s)
   with connection.urlopen(s) as data:
       output=data.read()
       print(output)
#    if "true" in output:
#      print("PROFANITY!!")
#    elif "false":
#      print("GOOOD")


textRead()
