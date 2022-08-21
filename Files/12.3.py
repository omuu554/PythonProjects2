
def ReadLines(File) :
        count = 0
        Line = File.readline().strip()
        while (Line):
            count += 1
            print(Line)
            Line = File.readline().strip()

        return count


with open("Story.txt", 'r') as File:
    print(ReadLines(File))