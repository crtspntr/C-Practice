#include <gtest/gtest.h>
#include "calc.h"

TEST(BasicLogicTest, EvenOdd) {
    EXPECT_TRUE(is_even(2));
    EXPECT_TRUE(is_even(0));
    EXPECT_FALSE(is_even(3));
    EXPECT_FALSE(is_even(-1));
}

TEST(BasicLogicTest, AdultCheck) {
    EXPECT_TRUE(is_adult(18));
    EXPECT_TRUE(is_adult(21));
    EXPECT_FALSE(is_adult(17));
    EXPECT_FALSE(is_adult(0));
}

TEST(BasicLogicTest, RangeCheck) {
    EXPECT_TRUE(is_in_range(5, 1, 10));
    EXPECT_TRUE(is_in_range(1, 1, 10));
    EXPECT_TRUE(is_in_range(10, 1, 10));
    EXPECT_FALSE(is_in_range(0, 1, 10));
    EXPECT_FALSE(is_in_range(11, 1, 10));
}
