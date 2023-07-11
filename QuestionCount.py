import os

current_directory = os.getcwd()
directories_count = sum(1 for item in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, item)))

print("Number of directories:", directories_count)