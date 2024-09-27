import debugpy
debugpy.listen(("0.0.0.0", 5678))  # Start the debug server on port 5678
print("Waiting for debugger attach")
debugpy.wait_for_client()  # Blocks execution until the debugger is attached
print("Debugger attached")

# Your main code follows here
print("helloworld")
