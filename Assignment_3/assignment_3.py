def readName(abhijit):
    with open("C:/Users/Admin/Desktop/DF_FUNDAMENTALS/Assignment_3/names.csv") as file:
        abhijit.append(file.read())

def loadMatrix(abhijit,mat):
    mat.extend(abhijit[0].strip().split('/n'))


def convertToColumnMajor(mat):
    temparary_number = []
    n = max([len(i) for i in mat])
    for i in range(n):
        res = ""
        for j in range(len(mat)):
            try:
                res += mat[j][i]

            except Exception as e:
                res += " "
        temparary_number.append(res.rstrip())
    mat.clear()
    mat.extend(temparary_number)


def calculateCharacterLength(mat):
    res = 0
    for i in mat:
        res += len(i)
    print("Total character length:", res)

def storeListAsString(mat):
    with open("abhijit_output.txt","wt") as file:
        for i in mat:
            file.write(i)


def main():
    abhijit = []
    mat = []
    readName(abhijit)
    loadMatrix(abhijit,mat)
    print("load matrix:",mat)
    convertToColumnMajor(mat)
    print("Column-major matrix:",mat)
    calculateCharacterLength(mat)
    storeListAsString(mat)
    print("file saved as abhijit_output.txt")

main()