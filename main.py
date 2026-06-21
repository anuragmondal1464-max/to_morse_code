# First make a dictionary of all the alphabets and there code. Like this : 

morse = {
    'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 
    'F': '.._.', 'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 
    'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 
    'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 
    'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 
    'Z': '__..' , " " : ""
}

# Let's take a input 

a = input("Enter The Sentence : ")

# Lets define the Function to convert .. 

def convert_to_morse(a):

    # Start a loop to get the alphabets ... 

    for i in a: 

        # Check if the alphabet is lower, if yes convert them in upper using .upper() function ... 

        if i.islower():
            b = i.upper()
            print(morse[b], end = "  ")

        else:

            # Now just simply convert them into morse ... 

            print(morse[i], end = "  ")

# Call out the function to test 

convert_to_morse(a)



