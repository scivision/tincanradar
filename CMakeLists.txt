cmake_minimum_required (VERSION 3.3)
project(chirp C CXX Fortran)

include(compiler.cmake) # boilerplate compiler flags
#------------
add_library(fwdmodel fwdmodel.f90 comm.f90)

add_executable(chirp test_chirp.f90)
target_link_libraries(chirp fwdmodel)

