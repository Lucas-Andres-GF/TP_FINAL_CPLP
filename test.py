try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("Ocurrio un error EOF.")
except IOError as e:
    print("Ocurrio un error IO.")