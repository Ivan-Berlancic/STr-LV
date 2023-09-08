import os
import shutil

testCSV = "Test.csv"
testDir = "C:/Users/Ivan/Desktop/lv8/archive/Test"

os.makedirs(testDir, exist_ok=True)

rows = open(testCSV).read().strip().split("\n")[1:]

for r in rows:
    (label, imagePath) = r.strip().split(",")[-2:]
    os.makedirs(os.path.join(testDir, label), exist_ok=True)
    shutil.copy(os.path.join("C:/Users/Ivan/Desktop/lv8/archive", imagePath), os.path.join(testDir,label))
