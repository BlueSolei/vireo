cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

set (CMAKE_CXX_STANDARD 14)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(helloworld helloworld.cpp)
target_link_libraries(helloworld ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME helloworld
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND helloworld)
