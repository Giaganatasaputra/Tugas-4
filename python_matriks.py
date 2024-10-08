# Fungsi untuk input matriks 3x3
def input_matrix(matrix_name):
    matrix = []
    print(f"Masukkan elemen {matrix_name} (3x3):")
    for i in range(3):
        row = []
        for j in range(3):
            element = float(input(f"Masukkan elemen [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Fungsi untuk menampilkan matriks
def display_matrix(matrix, matrix_name):
    print(f"{matrix_name} (3x3):")
    for row in matrix:
        print(row)

# Fungsi untuk menjumlahkan dua matriks
def add_matrices(matrix_a, matrix_b):
    result = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

# Fungsi untuk mengurangi dua matriks
def subtract_matrices(matrix_a, matrix_b):
    result = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result

# Fungsi untuk mengalikan dua matriks
def multiply_matrices(matrix_a, matrix_b):
    result = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

# Main program
if __name__ == "__main__":
    # Input matriks A dan B
    matrix_a = input_matrix("Matriks A")
    matrix_b = input_matrix("Matriks B")

    # Menampilkan matriks
    display_matrix(matrix_a, "Matriks A")
    display_matrix(matrix_b, "Matriks B")

    # Operasi
    sum_matrix = add_matrices(matrix_a, matrix_b)
    diff_matrix = subtract_matrices(matrix_a, matrix_b)
    product_matrix = multiply_matrices(matrix_a, matrix_b)

    # Menampilkan hasil
    display_matrix(sum_matrix, "Hasil Penjumlahan")
    display_matrix(diff_matrix, "Hasil Pengurangan")
    display_matrix(product_matrix, "Hasil Perkalian")

