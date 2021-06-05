F1 = "F1.txt"
F2 = "F2.txt"
with open (F1, "r") as file1:
    with open (F2, "w") as file2:
        i = 1
        lines = file1.readlines()

        for line in lines:
            if i > 3:
                file2.write(line)

            if i == len(lines):
                splitedline = line.split(" ")
                lastword = splitedline [len(splitedline) - 1]
                print (lastword)
                print(len(lastword))

            i += 1


