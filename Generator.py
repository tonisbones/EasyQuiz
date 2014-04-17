import json
import os

def readJson(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())
    return None
jsonFile = "sample"
jdict = readJson("json/%s.json" % jsonFile)
print(jdict["returnEmail"])
print(jdict["random"])
for problem in jdict["problems"]:
    print(problem["type"])
"""
#filename = os.path.join(os.getcwd(), "sample.json")
filename = "sample.json"
with open(filename, "r") as f:
    jdict = json.load(f)
print(jdict["returnEmail"])
"""
