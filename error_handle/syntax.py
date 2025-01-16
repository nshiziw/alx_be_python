try:
    # contains code that might potentially cause an exception
except ExceptionType:
    # Catches specific exceptions based on the ExceptionType. You can have multiple except blocks to handle different exception types.
else:
    # Executes code only if no exceptions occur within the try block.
finally:
    # Executes code regardless of whether an exception occurs or not. It’s commonly used for cleaning up resources like closing files.