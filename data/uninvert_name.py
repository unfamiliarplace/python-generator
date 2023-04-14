students = """Burton, Alice
Carone, Joshua
Cheng, Joshua
Fantilli, Carmela
Fraser, Destiny
Garcia, Mariam
Grootenboer, Meagan
Kang, Clementina
Kiervin-Starkey, Eliaura
Min, Joshua
Min, Joyce
Moorthy, Sharon
Nieuwstraten, Bethany
Solski, Trin
Stefanutti, Emma
Tenyenhuis, Allie
vanLenthe, Risa"""

students = students.split('\n')
for student in students:
    last, first = student.split(', ')
    student = ' '.join((first, last))
    print(student)

