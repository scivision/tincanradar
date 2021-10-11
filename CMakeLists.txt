cmake_minimum_required (VERSION 3.15...3.21)

project(FMCWchirp LANGUAGES Fortran)

include(CTest)

add_compile_options(
"$<$<COMPILE_LANG_AND_ID:Fortran,Intel,IntelLLVM>:-warn;-heap-arrays>"
"$<$<COMPILE_LANG_AND_ID:Fortran,GNU>:-fimplicit-none;-mtune=native;-Wall;-Wextra>"
)

add_library(fwdmodel OBJECT fwdmodel.f90 comm.f90)

add_executable(chirp test_chirp.f90)
target_link_libraries(chirp PRIVATE fwdmodel)

if(BUILD_TESTING)
  add_test(NAME FortranChirp COMMAND $<TARGET_FILE:chirp>)
  set_tests_properties(FortranChirp PROPERTIES TIMEOUT 10)
endif(BUILD_TESTING)
