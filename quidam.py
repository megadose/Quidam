#The Content has been made available for informational and educational purposes only
import argparse
from quidam import *

listModules = ["instagram","twitter","github"]

parser = argparse.ArgumentParser()
requiered = parser.add_argument_group('requiered arguments')
parser.add_argument('-u', '--username', help="The uername of the target",required=True)
parser.add_argument('-m', '--module', help="Modules to use instagram, twitter, github or all",required=True)
args = parser.parse_args()

#print("Quidam get email with recovery password")
print("You select "+args.module)

if args.module=="instagram":
    info = instagram(args.username)
    if '"status"' not in info:
        print("Email extract with instagram of "+args.username+": "+info)
    else:
        print(args.username+" account not found")

elif args.module=="twitter":
    info = twitter(args.username)
    if len(info)==2:
        print("The end of the phone number in twitter of "+args.username+": "+str(info["phone"]))
        print("Email extract with twitter of "+args.username+": "+info["email"])
    elif len(info)==1 :
        print("Email extract with twitter of "+args.username+": "+info["email"])
    else:
        print("Not informations found")

elif args.module=="github":
    info = github(args.username)
    if len(info)==0:
        print("Not informations found in github")
    else:
        print("All emails found in github :")
        for e in info:
            print("Email "+e["email"]+" for "+e["name"])

elif args.module=="all":
    info = instagram(args.username)
    if '"status"' not in info:
        print("Email extract with instagram of "+args.username+": "+info)
    else:
        print(args.username+" account not found")
    info = twitter(args.username)
    if len(info)==2:
        print("The end of the phone number in twitter of "+args.username+": "+str(info["phone"]))
        print("Email extract with twitter of "+args.username+": "+info["email"])
    elif len(info)==1 :
        print("Email extract with twitter of "+args.username+": "+info["email"])
    else:
        print("Not informations found")
    info = github(args.username)
    if len(info)==0:
        print("Not informations found in github")
    else:
        print("All emails found in github :")
        for e in info:
            print("Email "+e["email"]+" for "+e["name"])

else:
    print("List of modules :")
    for i in listModules:
        print(i)
