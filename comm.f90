module comm
use, intrinsic :: iso_c_binding, only: sp=>C_FLOAT, dp=>C_DOUBLE, i64=>C_LONG_LONG, sizeof=>c_sizeof, c_int

implicit none
public

integer,parameter :: wp=sp

complex(wp),parameter :: J=(0._wp,1._wp)
real(wp),parameter :: pi = 4._wp*atan(1._wp)
real(wp),parameter :: c = 299792458._wp

end module comm
