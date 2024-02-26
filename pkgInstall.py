# Create pkg inst.py when the packages are listed by the programmer
# Next implement the same for npm
import subprocess
import sys

pkg =[]

def Test():
    # getPkg(0)
    #getPkg()
    print("Ok")
    writepkg()

def getPkg():
    n=int(input("Enter Number of packages to append:"))
    for x in range(n):
        pkg.append(input("Enter Package Name:"))     
'''
def getPkg(num):
    n=num
    for x in range(n):
        print("Hello")
'''
        
def checkpkg(pkg):
    print("To Implement")


def writepkg():
    pg =["NAT","BAT","CAT"]

    f=open("pkg.py","w")
    f.writelines("def install():\n\ttry:\n\t\t")
    for x in pg:
       f.writelines("""subprocess.run(["pip", "install"," """+x+""""], check=True)\n\t\t""")
    f.write("""     
\texcept subprocess.CalledProcessError as e:
\t\tprint(f"Error: {e}")
\t\tsys.exit(1)
\tprint("Updated with Message:"+commit_message)
\ninstall()
""") # There was a tabspace above remember
    f.close()

def addpkg():
    print()

Test()