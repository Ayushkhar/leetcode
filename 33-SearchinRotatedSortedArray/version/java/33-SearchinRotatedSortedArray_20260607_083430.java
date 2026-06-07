// Last updated: 6/7/2026, 8:34:30 AM
1class Solution
2{
3    // Find pivot (minimum element index)
4    static int peak(int[] nums)
5    {
6        int n = nums.length;
7        int low = 0, high = n - 1;
8
9        while (low < high)
10        {
11            int mid = (low + high) / 2;
12
13            // If mid element is greater than high, pivot is to the right
14            if (nums[mid] > nums[high])
15            {
16                low = mid + 1;
17            }
18            else
19            {
20                high = mid;
21            }
22        }
23        return low; // index of smallest element
24    }
25
26    // Ascending binary search
27    int binaryAsc(int[] nums, int low, int high, int target)
28    {
29        while (low <= high)
30        {
31            int mid = (low + high) / 2;
32            if (nums[mid] == target) return mid;
33            if (nums[mid] < target) low = mid + 1;
34            else high = mid - 1;
35        }
36        return -1;
37    }
38
39    // Descending binary search
40    int binaryDesc(int[] nums, int low, int high, int target)
41    {
42        while (low <= high)
43        {
44            int mid = (low + high) / 2;
45            if (nums[mid] == target) return mid;
46            if (nums[mid] > target) low = mid + 1;
47            else high = mid - 1;
48        }
49        return -1;
50    }
51
52    public int search(int[] nums, int target)
53    {
54        int n = nums.length;
55        int pivot = peak(nums);
56
57        // Left half [0..pivot-1] is ascending
58        int left = binaryAsc(nums, 0, pivot - 1, target);
59        if (left != -1) return left;
60
61        // Right half [pivot..n-1] is ascending too (not descending)
62        return binaryAsc(nums, pivot, n - 1, target);
63    }
64}
65