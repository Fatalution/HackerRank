def split_and_join(line):
    line = line.split(' ')
    line = '-'.join(line)
    return line

line = raw_input()
result = split_and_join(line)
print result
