#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

z=cgi.FieldStorage("command")

op=z.getvalue("command")
lst=list()
lst=op.split()
if("date" in lst):
    output=sp.getoutput("date")
    print(output)
elif("cal" in lst or "calendar" in lst):
    output=sp.getoutput("cal")
    print(output)
elif("print" in lst or "cat" in lst):
    print("The content in the {} is :\n\n".format(lst[1]))
    ele=lst[1]
    output=sp.getoutput("sudo cat {}".format(ele))
    print(output)
elif ("docker" in lst):
    if ("run" in lst or "launch" in lst or "create" in lst):
        print("Launching....\n")
        output=sp.getstatusoutput("sudo docker run -dit --name containerrr httpd")
        if (output[0]==0):
            print(output)
        else:
            print("Sorry! The requested command can't be processed")
    elif ("start" in lst or "run" in lst) and ("docker" in lst):
        output=sp.getoutput("sudo systemctl start docker")
        print(output)
    elif ("stop" in lst or "discard" in lst or "disable" in lst):
        print("Stopping instance....\n")
        output=sp.getstatusoutput("sudo docker stop container ")
        if (output[0]==0):
            print(output)
        else:
            print("Sorry! The requested command can't be processed")

    elif (("check" in lst and "containers" in lst) or ("list" in lst and "conainers" in lst) or ("list all containers" in lst)):
        print("The containers launched are....\n")
        output=sp.getoutput("sudo docker ps")
        print(output)
    elif ("images" in lst or "check images" in lst):
        print("The imagess downloaded are....\n")
        output=sp.getoutput("sudo docker images")
        print("Docker images are:")
        print(output)
elif ("ls" in lst or "list" in lst):
    print("This is the list: ")
    output=sp.getoutput("ls")
    print(output)
elif ("present" in lst or "current" in lst) and ("directory" in lst or "folder" in lst or "dir" in lst):
    output=sp.getoutput("pwd")
    print(output)
elif ("configure" in lst) and ("webserver" in lst or "apache" in lst) and ("webpage" in lst):
    output=sp.getoutput("sudo yum install httpd -y ; sudo systemctl start httpd ; cd /var/www/html ; sudo cp /root/web_page.html /var/www/html/")
    print(output)
else:
    print("Invalid Input!!!!")
