cmake_minimum_required(VERSION 3.16)
project(CPPPractice LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(FetchContent)

FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/release-1.12.1.zip
)
FetchContent_MakeAvailable(googletest)

add_library(cpppractice_lib src/calc.cpp)
target_include_directories(cpppractice_lib PUBLIC include)

include(CTest)
if(BUILD_TESTING)
  file(GLOB_RECURSE TEST_SOURCES "tests/*.cpp")
  foreach(test_source ${TEST_SOURCES})
    get_filename_component(test_name ${test_source} NAME_WE)
    add_executable(${test_name} ${test_source})
    target_link_libraries(${test_name} PRIVATE cpppractice_lib GTest::gtest_main)
    gtest_discover_tests(${test_name})
  endforeach()
endif()

enable_testing()

