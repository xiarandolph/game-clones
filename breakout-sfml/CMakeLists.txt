cmake_minimum_required(VERSION 3.1)

project(breakout)

## If you want to link SFML statically
set(SFML_STATIC_LIBRARIES TRUE)

## In most cases better set in the CMake cache
#set(SFML_DIR "<sfml root directorty>/lib/cmake/SFML")

add_subdirectory(external/SFML-2.5.1)

include_directories(include)

set(SOURCE_FILES
    ./src/main.cpp
)

#find_package(SFML 2.5 COMPONENTS graphics audio REQUIRED)
add_executable(breakout ${SOURCE_FILES})
target_link_libraries(breakout sfml-graphics sfml-audio)
