class Matrix:

    def __init__(self, some_list: list):
        self.some_list = some_list

    def __str__(self):
        stroke = str()
        for i in range(0, len(self.some_list)):
            stroke_i = str()
            for j in range(0, len(self.some_list[i])):
                if j < len(self.some_list[i]) - 1:
                    stroke_i = stroke_i + str(self.some_list[i][j]) + ' '
                else:
                    stroke_i = stroke_i + str(self.some_list[i][j])
            stroke_j = f'|{stroke_i}|\n'
            stroke = stroke + stroke_j
        return f'{stroke}'

    def __add__(self, other):
        full_stroke = str()
        for k in range(0, len(self.some_list)):
            half_stroke_k = str()
            c = list(map(sum, zip(self.some_list[k], other.some_list[k])))
            for z in range(0, len(c)):
                if z < len(c) - 1:
                    half_stroke_k = half_stroke_k + str(c[z]) + ' '
                else:
                    half_stroke_k = half_stroke_k + str(c[z])
            full_stroke_k = f'|{half_stroke_k}|\n'
            full_stroke = full_stroke + full_stroke_k
        return full_stroke


first_matrix = [[18, 15, 48], [12, 14, 16]]
second_matrix = [[3, 5, 8], [25, 16, 100]]
a = Matrix(first_matrix)
print(a)
b = Matrix(second_matrix)
print(b)
print(a + b)
