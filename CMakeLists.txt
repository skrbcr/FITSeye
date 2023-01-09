cmake_minimum_required(VERSION 3.14)
project(fitseye)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# set(CMAKE_C_STANDARD 17)
# set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_COMPILER /usr/bin/clang)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_COMPILER /usr/bin/clang++)
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fuse-ld=lld")

find_package(wxWidgets COMPONENTS core base REQUIRED)
# Google Test (required if you run test)
find_package(GTest)
include(${wxWidgets_USE_FILE})

# FITS eye
add_executable(${PROJECT_NAME} fitseye/base.cpp fitseye/fits.cpp)
target_link_libraries(${PROJECT_NAME} ${wxWidgets_LIBRARIES} cfitsio)
target_compile_options(${PROJECT_NAME} PRIVATE
    -Wall -Wextra
    $<$<CONFIG:Debug>: -O0 -g3 -ggdb>
)

# Example
add_executable(ex_fits fitseye/fits.cpp example/fits.cpp)
target_link_libraries(ex_fits cfitsio)
target_compile_options(ex_fits PRIVATE
    -Wall -Wextra
    $<$<CONFIG:Debug>: -O0 -g3 -ggdb>
)

# Test
enable_testing()
add_executable(test_fits fitseye/fits.cpp test/fits.cpp)
# target_include_directories(test_fits )
target_link_libraries(test_fits
    ${wxWidgets_LIBRARIES} cfitsio
    GTest::gtest GTest::gtest_main
    # $<IF:$<VERSION_GREATER_EQUAL:${CMAKE_VERSION},3.20>, GTest::gtest, GTest::GTest>
)
add_test(COMMAND test_fits)
target_compile_options(test_fits PRIVATE
    -Wall -Wextra
    $<$<CONFIG:Debug>: -O0 -g3 -ggdb>
)

