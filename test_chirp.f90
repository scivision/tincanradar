program test_chirp

use fwdmodel, only: chirp
use comm, only: sp,stdout,c_int!,stderr

implicit none

real(sp),parameter :: bm=100e6 !Hz
real(sp),parameter :: tm=0.01 !second
real(sp),parameter :: fs=100e6 !Hz
real(sp),parameter :: nlfm=0.

integer(c_int),parameter  :: Ntarg = 2
real(sp),parameter :: Atarg(Ntarg)=[0.001,0.002]
real(sp),parameter :: range_m(Ntarg)=[5,7]

integer(c_int),parameter :: Ns=int(tm*fs)
complex(sp) :: y(Ns,Ntarg)
real(sp) :: t(Ns)
integer(c_int) :: i

write(stdout,*) Ns,' samples'

! time vector
do concurrent (i=1:Ns)
    t(i) = (i-1)/fs
enddo

call chirp(bm,tm,t,Ns,range_m,Atarg,Ntarg,nlfm,y)



end program test_chirp
