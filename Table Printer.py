tableData = [['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]
maxlen = 0
for fruit,name,animal in zip(tableData[0], tableData[1], tableData[2]):
    maxlen = max(len(fruit) + len (name) + len (animal), maxlen)
for fruit,name,animal in zip(tableData[0], tableData[1], tableData[2]):
    length = len(fruit) + len (name) + len (animal) 
    print (' ' * (maxlen - length) + fruit, name, animal)
