import subprocess

print("Enter the name of internet domain")
dom = input(":")
print("Enter the number of pings")
pi = int(input(":"))

print(subprocess.run(['ping -c {} {}'.format(pi, dom)], shell=True))