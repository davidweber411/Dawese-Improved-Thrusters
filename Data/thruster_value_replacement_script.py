import re

sbcFilePath = "deine_datei.xml"
multiplierFactor = 3

# read sbc with with xml content. 
with open(sbcFilePath, "r", encoding="utf-8") as file:
    content = file.read()

# regex pattern definition 
pattern = r"<ForceMagnitude>(\d+(\.\d+)?)<\/ForceMagnitude>"

# multiply value function 
def multiply_by_three(match):
    number = float(match.group(1))
    new_number = number * multiplierFactor
    return f"<ForceMagnitude>{new_number}</ForceMagnitude>"

# replace all values
new_content = re.sub(pattern, multiply_by_three, content)

# save the file again
with open(sbcFilePath, "w", encoding="utf-8") as file:
    file.write(new_content)

print("Ersetzung abgeschlossen!")
