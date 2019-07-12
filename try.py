board = [[1,2],[3,4]]
lis = list(filter(lambda x:x.count(6) != 0, board))

print(len(lis))
