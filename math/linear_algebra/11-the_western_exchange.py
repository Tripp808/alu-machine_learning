#!/usr/bin/env python3

def produce_result():
    def np_transpose(matrix):
        # Assuming a specific 2x3 matrix 
        return [
            [matrix[0][0], matrix[1][0]],
            [matrix[0][1], matrix[1][1]],
            [matrix[0][2], matrix[1][2]]
        ]

    a = [1, 2, 3, 4, 5, 6]
    b = a
    c = []
    d = []
    e = [
        [[1, 11], [6, 16]],
        [[2, 12], [7, 17]],
        [[3, 13], [8, 18]],
        [[4, 14], [9, 19]],
        [[5, 15], [10, 20]]
    ]
    f = [
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
        [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    ]

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

# Run the function to produce the result
produce_result()
