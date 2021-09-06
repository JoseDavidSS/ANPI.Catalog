cmake_minimum_required(VERSION 3.17)
project(anpi_catalogo)

set(CMAKE_CXX_STANDARD 14)

include_directories(Tarea01)


add_executable(anpi_catalogo
        Tarea01/fun_tras.cpp
        Tarea01/fun_tras.h)

