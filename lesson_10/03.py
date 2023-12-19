# f = open('test.txt', 'w')
# ...
# f.close()
#
#
# try:
#     f = open('test.txt', 'w')
#     ...
# finally:
#     f.close()
#
#
# with open('test.txt') as f:
#     ...


# ff = open('test.txt', 'r')
# a = ff.read()
# ff.close()
#
# print(a)

# with open('test.txt') as f:
#     a = f.read(12)
#     f.seek(0)
#     b = f.read(5)
#     f.seek(0)
#     print(f.read(5))
#     f.seek(0)
#     print(f.read(5))
#     f.seek(0)
#     print(f.read(5))
# print(a)
# print(b)


try:
    f = open('test.txt', 'r')
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())
finally:
    f.close()


try:
    f = open('test.txt', 'r')
    print(f.readlines())
finally:
    f.close()
