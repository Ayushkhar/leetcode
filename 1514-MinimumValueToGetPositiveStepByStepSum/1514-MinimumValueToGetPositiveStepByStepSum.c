// Last updated: 6/6/2026, 10:24:50 PM
#include <stdio.h>

int minStartValue(int *nums, int n) {
    int minsum = 0;
    int psum = 0;
    
    for (int i = 0; i < n; i++) {
        psum += nums[i];
        if (psum < minsum) {
            minsum = psum;
        }
    }
    
    return 1 - minsum;
}


