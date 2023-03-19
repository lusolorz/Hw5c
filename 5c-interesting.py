#run 
import subprocess

def main():
    print("hello")

    # Define the command to run
    command = ['./is-interesting-helper']

    # Run the command and capture its output
    output = subprocess.run(command, shell= True)

    # Parse the output to extract the coverage value
    x = int(output.strip())

    # Print the value of x
    print("The coverage value is",x)

#only decrease if removing test suites
#may have to run compoundly so that we can get the coveage for the whole subset not the individual subset

if __name__ == '__main__':
    main()
