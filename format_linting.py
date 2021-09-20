#  Formating and Linting

# Formatting
#   Makes  code readable 
#   easier to debug
#   consistency helps everyone

# pep 8 rules
#   * Spacces no Tab
#   * variable_name not variableName/VariableName
#   * Avoid extraneous white space
        # {'good': 43}
        # {'bad': 21}
#   * consistent in format

# lint
# -identify format issues
#  add linter "pip install pylint"

# docstring 
# -for inline documentation
# """
# """

def print_hello(name:str)-> str:
    """
    Greet the user by name

    Parameter:
        name (str): The name of the user 
    Returns: 
        str: The Greeting 
    """
    print('Hello, '+ name)


# Type hints
# -tell editor and linter what data types to expect
def get_greeting(name:str) -> str:
    print('Hello, '+ name)

