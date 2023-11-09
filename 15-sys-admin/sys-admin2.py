import subprocess

print("________________________________________________________________________ls")
subprocess.run(["ls"])

print("\n________________________________________________________________________ls -l")
subprocess.run(["ls","-l"])

print("\n________________________________________________________________________ls -l README.md")
subprocess.run(["ls","-l","README.md"])

print("\n________________________________________________________________________uname -a")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print("\n________________________________________________________________________ps -x")
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])