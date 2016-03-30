SRC=comm.f90 fwdmodel.f90
MAIN=test_chirp.f90
#----------------
FC = gfortran 
F2PY = f2py3

FFLAGS = -std=f2008 -Wall -Wpedantic -Wextra -mtune=native -fexternal-blas -ffast-math -O3


OBJS=$(SRC:.f90=.o)
MOBJS=$(OBJS) $(MAIN:.f90=.o)

%.o: %.f90
	$(FC) $(FFLAGS) -c $<

all: chirp.out pychirp

chirp.out: $(MOBJS)
	$(FC) -o $@ $(MOBJS) $(FFLAGS)

pychirp: $(SRC)
	$(F2PY) --quiet -m $@ -c $(SRC)

clean:
	$(RM) $(MOBJS)

