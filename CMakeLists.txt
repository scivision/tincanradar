cmake_minimum_required (VERSION 3.7)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Debug or Release")
endif()

project(FMCWchirp LANGUAGES Fortran)

include(CTest)

if(CMAKE_Fortran_COMPILER_ID STREQUAL Intel)
  if(WIN32)
    string(APPEND CMAKE_Fortran_FLAGS " /warn /stand:f18 /heap-arrays")
  else()
    string(APPEND CMAKE_Fortran_FLAGS " -warn -stand f18  -heap-arrays")
  endif()
elseif(CMAKE_Fortran_COMPILER_ID STREQUAL GNU)
  if(CMAKE_Fortran_COMPILER_VERSION VERSION_GREATER_EQUAL 8.1)
  string(APPEND CMAKE_Fortran_FLAGS " -std=f2018")
  endif()

  string(APPEND CMAKE_Fortran_FLAGS " -fimplicit-none -mtune=native -Wall -Wextra")
endif()
#------------
add_library(fwdmodel OBJECT fwdmodel.f90 comm.f90)

add_executable(chirp test_chirp.f90)
target_link_libraries(chirp PRIVATE fwdmodel)
if(BUILD_TESTING)
add_test(NAME FortranChirp COMMAND chirp)
set_tests_properties(FortranChirp PROPERTIES TIMEOUT 10)
endif(BUILD_TESTING)
