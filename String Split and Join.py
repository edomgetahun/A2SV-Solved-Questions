def split_and_join(line):
    string2= line.split(" ")
    return "-".join(string2)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
