
def helloWorld():
    print('Hello World')
    
helloWorld()


def print_arguments():
    script_name = sys.argv[0]
    variables = sys.argv[1:]
    print("Script name:", script_name)
    print("Variables:", variables)
    
    
print("Script and Variables:", script_name, variables)
