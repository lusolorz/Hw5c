#run 
import subprocess
import re

def main():
    print("hello")

    # Define the command to run
    command = ['./is-interesting-helper']

    # Run the command and capture its output
    temp = subprocess.run(command, shell= True)
    file1 = open(r"/home/ubuntu/Hw5c/libpng/png-test-summary.txt", "r")
    output = file1.read()
    # Parse the output to extract the coverage value
    #x = int(output.strip())
    reg = '.*10606$'
    str = re.findall(reg, output)

    # Print the value of x
    print("The coverage value is",str[0][15:20])

#only decrease if removing test suites
#may have to run compoundly so that we can get the coveage for the whole subset not the individual subset

if __name__ == '__main__':
    main()
