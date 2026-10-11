#include "calc.h"

bool is_even(int n) {

    return (n % 2 == 0);
}

bool is_adult(int age) {
    
    return (age >= 18);
}

bool is_in_range(int value, int low, int high) {
    
    return (value >= low && value <= high);
}
