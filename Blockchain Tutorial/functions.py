def unlimited_arguments(*args, **keyword_args): #unpacking with * for lists/tuples or ** for dictionaries
    print(args)
    for k, argument in keyword_args:
        print(k, argument)

unlimited_arguments(1,2,3,4, name = 'Max', age=29)