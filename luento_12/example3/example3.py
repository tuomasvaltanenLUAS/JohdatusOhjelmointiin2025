# text submission grading code
# * is a bad char -> penalty, otherwise add points
addition = 5
penalty = addition * -1

# test values, should come from data API later
submissions = [["AB", "CE*", "FF", "EE*", "EE", "EE", "EE", "EE", "EE"],
               ["A*B", "CE*", "*FF", "EE", "EE", "EE", "EE"],
               ["AB", "CE*", "FF", "HJ", "AY", "UU", "FF", "FF", "FF", "FF*"]]

areas = {"0-19": "Low", "20-29": "Middle", "30-39": "High"}
results = []

selection = int(input("Amount of cycles: \n"))
print()

max_range = (selection, len(submissions))[selection > (len(submissions) - 1)]

# loop submissions
for sub in range(max_range):
    score = 0
    for state in submissions[sub]: score += penalty if "*" in state else addition
    results.append(score)

# loop results
for r in results:
    for i in areas.keys(): print(areas[i], f"\t({r} pts)", "\t-> ", ", ".join(submissions[results.index(r)])) \
        if int(i.split("-")[0]) <= r <= int(i.split("-")[1]) else print("", end="")