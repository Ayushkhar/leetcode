// Last updated: 6/6/2026, 10:26:28 PM
void insertion(int *nums, int numsize) {
    for (int i = 1; i < numsize; i++) {
        int temp = nums[i];
        int j = i - 1;
        while (j >= 0 && nums[j] > temp) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = temp;
    }
}

int majorityElement(int* nums, int numsSize) {
    insertion(nums, numsSize);
    int count = 1;
    int candidate = nums[0];
    
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == candidate) {
            count++;
        } else {
            count = 1;
            candidate = nums[i];
        }
        if (count > numsSize / 2) {
            return candidate;
        }
    }
    return candidate;
}