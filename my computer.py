import platform

# Retrieve the computer properties using the platform module
os_name = platform.system()
os_version = platform.release()
processor = platform.processor()
machine = platform.machine()
node = platform.node()

# Print the computer properties to the terminal
print("Operating System:", os_name)
print("OS Version:", os_version)
print("Processor:", processor)
print("Machine Type:", machine)
print("Hostname:", node)
