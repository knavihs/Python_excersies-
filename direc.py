import os
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
             print(os.path.join(root, file))