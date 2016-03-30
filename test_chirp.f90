program test_chirp

use fwdmodel, only: chirp
use comm, only: dp,stdout!,stderr

implicit none

real(dp),parameter :: bm=100e6 !Hz
real(dp),parameter :: tm=0.01 !second
real(dp),parameter :: fs=100e6 !Hz
real(dp),parameter :: nlfm=0.

integer,parameter  :: Ntarg = 2
real(dp),parameter :: Atarg(Ntarg)=[0.001,0.002]
real(dp),parameter :: range_m(Ntarg)=[5,7]

integer,parameter :: Ns=int(tm*fs)
complex(dp) :: y(Ns,Ntarg)
real(dp) :: t(Ns)
integer :: i

write(stdout,*) Ns,' samples'

! time vector
do i=1,Ns
    t(i) = (i-1)/fs
enddo

call chirp(bm,tm,t,Ns,range_m,Atarg,Ntarg,nlfm,y)





end program test_chirp
