cmake_minimum_required (VERSION 3.15...3.29)

project(FMCWchirp LANGUAGES Fortran)

enable_testing()

add_compile_options(
"$<$<COMPILE_LANG_AND_ID:Fortran,Intel,IntelLLVM>:-warn;-heap-arrays>"
"$<$<COMPILE_LANG_AND_ID:Fortran,GNU>:-fimplicit-none;-Wall>"
)

add_library(fwdmodel OBJECT fwdmodel.f90 comm.f90)

add_executable(chirp test_chirp.f90)
target_link_libraries(chirp PRIVATE fwdmodel)

# "pychirp", sources=["comm.f90", "fwdmodel.f90"]

add_test(NAME FortranChirp COMMAND chirp)
