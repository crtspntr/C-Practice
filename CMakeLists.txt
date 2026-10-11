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
  add_executable(cpppractice_tests tests/calc_test.cpp)
  target_link_libraries(cpppractice_tests PRIVATE cpppractice_lib GTest::gtest_main)
  include(GoogleTest)
  gtest_discover_tests(cpppractice_tests)
endif()

enable_testing()
