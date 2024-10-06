BEGIN

    FUNCTION InputMatrix(matrixName)
        DECLARE matrix[3][3]
        PRINT "Masukkan elemen " + matrixName + " (3x3):"
        
        FOR i FROM 0 TO 2 DO
            FOR j FROM 0 TO 2 DO
                PRINT "Masukkan elemen [" + (i+1) + "][" + (j+1) + "]: "
                READ matrix[i][j]
            END FOR
        END FOR
        
        RETURN matrix
    END FUNCTION

    FUNCTION DisplayOrder(matrix)
        rows = LENGTH(matrix)
        cols = LENGTH(matrix[0]) // Jika ada baris
        PRINT "Orde Matriks: " + rows + "x" + cols
    END FUNCTION

    // Main program
    DECLARE matrixA[3][3]
    DECLARE matrixB[3][3]

    matrixA = InputMatrix("Matriks A")
    matrixB = InputMatrix("Matriks B")

    DisplayOrder(matrixA)
    DisplayOrder(matrixB)

END
