cmake_minimum_required (VERSION 2.8)
project(chirp C CXX Fortran)

add_compile_options(-std=f2008 -mtune=native -Wall -Wextra -Wpedantic -fexceptions)
#------------
add_library(fwdmodel fwdmodel.f90 comm.f90)

add_executable(chirp test_chirp.f90)
target_link_libraries(chirp fwdmodel)

