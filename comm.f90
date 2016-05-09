module comm
use, intrinsic :: iso_c_binding, only: sp=>C_FLOAT, dp=>C_DOUBLE, i64=>C_LONG_LONG, sizeof=>c_sizeof, c_int

use, intrinsic :: iso_fortran_env, only : stdout=>output_unit, stderr=>error_unit

implicit none
    public

    complex(sp),parameter :: J=(0.,1.)
    real(sp),parameter :: pi = 4.*atan(1.)
    real(sp),parameter :: c = 299792458.

contains

    subroutine init_random_seed()

        integer(c_int) :: i, n, clock
        integer(c_int), allocatable :: seed(:)

        call random_seed(size=n)
        allocate(seed(n))
        call system_clock(count=clock)
        seed = clock + 37 * [ (i - 1, i = 1, n) ]
        call random_seed(put=seed)
    end subroutine

end module comm
