#you need to import the webbrowser module for launching the browser and import the sys module for reading the potential command line arguments.
import webbrowser, sys

prompt = input("What is your address?: ")
your_address = prompt
webbrowser.open(f'https://www.google.com/maps/place/{your_address}')

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.
