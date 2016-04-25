#this is a Cmake>=3.3 template, loaded with include(compiler.cmake) from your main CMakeLists.txt
add_compile_options(-mtune=native -Wall -Wextra -Wpedantic -fexceptions)

add_compile_options("$<$<CONFIG:RELEASE>:-ffast-math>")

if (NOT CYGWIN)
    add_compile_options(-fstack-protector-all)
endif()

set(fortran_flags -std=f2008)


#-Warray-temporaries -Winteger-division -funroll-loops

if (CMAKE_CXX_COMPILER_ID MATCHES Clang)
    list(APPEND ccxx_flags -Weverything -Werror=array-bounds -Wno-c++98-compat)
elseif(CMAKE_CXX_COMPILER_ID MATCHES GNU)
    list(APPEND ccxx_flags -Warray-bounds=2)
elseif(CMAKE_CXX_COMPILER_ID MATCHES Intel)
    list(APPEND ccxx_flags -check bounds -fpe0 -traceback)
endif()

if(CMAKE_Fortran_COMPILER_ID MATCHES GNU)
    list(APPEND fortran_flags -fbacktrace -Warray-bounds=2)
elseif(CMAKE_Fortran_COMPILER_ID MATCHES Intel)
    list(APPEND fortran_flags -traceback -fpe0)
elseif(CMAKE_Fortran_COMPILER_ID MATCHES PGI)
    list(APPEND fortran_flags -traceback)
endif()

add_compile_options( # Cmake >=3.3 for COMPILE_LANGUAGE
    "$<$<COMPILE_LANGUAGE:C>:${ccxx_flags}>"
    "$<$<COMPILE_LANGUAGE:CXX>:${ccxx_flags}>"
    "$<$<COMPILE_LANGUAGE:Fortran>:${fortran_flags}>"
)


# https://gcc.gnu.org/onlinedocs/gcc-5.3.0/gcc/Debugging-Options.html
if(CMAKE_BUILD_TYPE MATCHES Debug)
#    add_compile_options(-fsanitize=address)
endif()
