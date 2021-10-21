def decimal2binary(value):
    return [int (element) for element in bin(value)[2:].zfill(8)]

print(decimal2binary(10))