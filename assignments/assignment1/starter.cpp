#include "calc.h"

// Starter: intentionally a stub you can replace and improve.
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);  // correct but slow
}

int clamp_value(int value, int low, int high) {
    if (low > high) {
        // naive swap
        int tmp = low; low = high; high = tmp;
    }
    if (value < low) return low;
    if (value > high) return high;
    return value;
}
