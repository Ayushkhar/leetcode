// Last updated: 6/16/2026, 9:28:56 PM
class Solution
{
    // Find pivot (minimum element index)
    static int peak(int[] nums)
    {
        int n = nums.length;
        int low = 0, high = n - 1;

        while (low < high)
        {
            int mid = (low + high) / 2;

            // If mid element is greater than high, pivot is to the right
            if (nums[mid] > nums[high])
            {
                low = mid + 1;
            }
            else
            {
                high = mid;
            }
        }
        return low; // index of smallest element
    }

    // Ascending binary search
    int binaryAsc(int[] nums, int low, int high, int target)
    {
        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

    // Descending binary search
    int binaryDesc(int[] nums, int low, int high, int target)
    {
        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

    public int search(int[] nums, int target)
    {
        int n = nums.length;
        int pivot = peak(nums);

        // Left half [0..pivot-1] is ascending
        int left = binaryAsc(nums, 0, pivot - 1, target);
        if (left != -1) return left;

        // Right half [pivot..n-1] is ascending too (not descending)
        return binaryAsc(nums, pivot, n - 1, target);
    }
}
