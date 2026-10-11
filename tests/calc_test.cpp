#include <gtest/gtest.h>
#include "calc.h"

TEST(CalcTest, FibonacciSmallValues) {
    EXPECT_EQ(fibonacci(0), 0);
    EXPECT_EQ(fibonacci(1), 1);
    EXPECT_EQ(fibonacci(10), 55);
}

TEST(CalcTest, ClampBehaves) {
    EXPECT_EQ(clamp_value(5, 1, 10), 5);
    EXPECT_EQ(clamp_value(-3, 0, 9), 0);
    EXPECT_EQ(clamp_value(50, 0, 9), 9);
}
