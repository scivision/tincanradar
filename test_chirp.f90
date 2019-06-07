use fwdmodel, only: chirp
use comm, only: wp,c_int

implicit none

real(wp),parameter :: bm=10e6_wp !Hz
real(wp),parameter :: tm=0.01_wp !second
real(wp),parameter :: fs=10e6_wp !Hz
real(wp),parameter :: nlfm=0._wp

integer(c_int),parameter  :: Ntarg = 2
real(wp),parameter :: Atarg(Ntarg)=[0.001_wp, 0.002_wp]
real(wp),parameter :: range_m(Ntarg)=[5._wp, 7._wp]

integer(c_int),parameter :: Ns=int(tm*fs)
complex(wp) :: y(Ns,Ntarg)
real(wp) :: t(Ns)
integer(c_int) :: i

print *, Ns,' samples'

! time vector
do concurrent (i=1:Ns)
  t(i) = (i-1)/fs
enddo

call chirp(bm,tm,t,Ns,range_m,Atarg,Ntarg,nlfm,y)

end program
