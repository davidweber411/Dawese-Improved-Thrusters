import re

def replace_force_magnitudes(file_paths):
    multiplierFactor = 3

    for sbcFilePath in file_paths:
        with open(sbcFilePath, "r", encoding="utf-8") as file:
            content = file.read()

        pattern = r"<ForceMagnitude>(\d+(\.\d+)?)<\/ForceMagnitude>"

        def multiply_by_three(match):
            number = float(match.group(1))
            new_number = int(number * multiplierFactor)
            return f"<ForceMagnitude>{new_number}</ForceMagnitude>"

        new_content = re.sub(pattern, multiply_by_three, content)

        with open(sbcFilePath, "w", encoding="utf-8") as file:
            file.write(new_content)

        print(f"Ersetzung abgeschlossen für {sbcFilePath}!")

replace_force_magnitudes([
    "CubeBlocks_Thrusters.sbc", 
    "CubeBlocks_IndustrialPack.sbc", 
    "CubeBlocks_SparksOfTheFuturePack.sbc",
    "CubeBlocks_Warfare2.sbc"
    ])

# sbcFilePath = "CubeBlocks_Thrusters.sbc"
# sbcFilePath = "CubeBlocks_IndustrialPack.sbc"
# sbcFilePath = "CubeBlocks_SparksOfTheFuturePack.sbc"
# sbcFilePath = "CubeBlocks_Warfare2.sbc"