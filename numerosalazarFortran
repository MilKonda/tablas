program generar_numeros_azar
    implicit none
    integer :: i, num
    real :: num_real

    call random_seed()  ! Inicializar la semilla del generador de números aleatorios

    do i = 1, 10
        call random_number(num_real)  ! Generar un número aleatorio entre 0 y 1
        num = int(num_real * 100) + 1  ! Escalar a un rango de 1 a 100 y convertir a entero
        write(*, '(I4)', advance='no') num  ! Mostrar el número como entero
        if (i < 10) then
            write(*, '(A)', advance='no') " "  ! Imprimir espacio sin salto de línea
        end if
    end do

    print *  ! Salto de línea al final
end program generar_numeros_azar
