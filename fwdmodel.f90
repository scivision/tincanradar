module fwdmodel
use comm,only: J,wp,c_int,pi,c
implicit none

private
public:: chirp, chirp_phase
contains


pure subroutine chirp(bm,tm,t,Ns,range_m,Atarg,Ntarg,nlfm,y)

integer(c_int), intent(in) :: Ns,Ntarg
real(wp), intent(in) ::  bm,tm,t(Ns),range_m(Ntarg),Atarg(Ntarg),nlfm
complex(wp),intent(out) :: y(Ns)

complex(wp) :: LO(Ns)
real(wp) ::  phase(Ns), toffs(Ntarg)
integer :: i

toffs = 2*range_m/c !two-way delay

call chirp_phase(bm,tm,t,Ns,nlfm,phase)
! radar transmit
LO = exp(J*phase)
! generate target returns
y = 0.
do concurrent (i=1:Ntarg)
  call chirp_phase(bm,tm,t+toffs(i),Ns,nlfm,phase)
  y = y + Atarg(i) * exp(J*phase) * conjg(LO)
enddo

end subroutine chirp

pure subroutine chirp_phase(bm,tm,t,Ns,nlfm,phase)

integer(c_int), intent(in) :: Ns
real(wp), intent(in) :: bm,tm,nlfm,t(Ns)
real(wp), intent(out):: phase(Ns)

real(wp) :: B1, B2

B1 = bm / tm
B2 = bm / tm**2

phase = 2._wp*pi*(-0.5_wp*bm*t   &       !starting freq
         + 0.5_wp*B1*t**2      & !linear ramp ("derivative of phase is frequency")
         + 0.5_wp*nlfm*B2*t**3)  !quadratic frequency

end subroutine chirp_phase

end module fwdmodel
