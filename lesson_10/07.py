with open('test_2.txt', 'w', encoding='Latin_1') as f:
    f.write('SFET ewf de bawk rg\nsjfgjsdfeg sjdghjs fd\nghjghghgcsfgrfw\n')



with open('test_2.txt', 'wb') as f:
    f.write('SFET ewf de bawk rg\nsjfgjsdfeg sjdghjs fd\nghjghghgcsfgrfw\n'.encode())

with open('test_3.txt', 'wb') as f:
    f.write(b'345FFREd345667ASSDFGVBNJ')
