def count_lines():
    
    while True:
        filename = input('Enter a filename: ')
        
        try:
            file = open(filename, 'r')
            break
        except(FileNotFoundError):
            print("Couldn't find that file.")
            
    lines = 0
    for line in file:
        line = line.strip()
        lines += bool(line)
    file.close()
    
    print('{} non-empty lines.'.format(lines))
        
count_lines()