import subprocess

print("Check problems with systemctl")
print("Enter the name of internet domain")
program = input(":")
print("Choose: status, reload, stop, start or else")
stat = input(":")

print(subprocess.run([' sudo systemctl {} {}'.format(stat, program)], shell=True))