cmake_minimum_required(VERSION 3.22)
project(fitseye)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_COMPILER clang++)

find_package(wxWidgets COMPONENTS core base REQUIRED)
include(${wxWidgets_USE_FILE})

add_executable(${PROJECT_NAME} src/base.cpp)
target_link_libraries(${PROJECT_NAME} ${wxWidgets_LIBRARIES} cfitsio)
target_compile_options(${PROJECT_NAME} PRIVATE
    -Wall -Wextra
    $<$<CONFIG:Debug>: -O0 -g3 -ggdb>
)

