// Last updated: 6/7/2026, 8:25:36 AM
1class Solution
2{
3    // Find pivot (index of largest element)
4    static int peak(int[] nums)
5    {
6        int n = nums.length;
7
8        if (n == 1) return 0;
9
10        int low = 0;
11        int high = n - 1;
12
13        while (low < high)
14        {
15            int mid = (low + high) / 2;
16
17            // If mid element is greater than high, pivot is to the right
18            if (nums[mid] > nums[high])
19            {
20                low = mid + 1;
21            }
22            else
23            {
24                high = mid;
25            }
26        }
27
28        // low == high → index of smallest element (rotation pivot)
29        return low;
30    }
31
32    // Standard binary search
33    int binary(int[] nums, int low, int high, int target) 
34    {
35        while (low <= high)
36        {
37            int mid = (low + high) / 2;
38
39            if (nums[mid] == target)
40            {
41                return mid;
42            }
43
44            if (nums[mid] < target)
45            {
46                low = mid + 1;
47            }
48            else
49            {
50                high = mid - 1;
51            }
52        }
53
54        return -1;
55    }
56
57    public int search(int[] nums, int target)
58    {
59        int n = nums.length;
60        int pivot = peak(nums);
61
62        // If target lies in right sorted half
63        if (target >= nums[pivot] && target <= nums[n - 1])
64        {
65            return binary(nums, pivot, n - 1, target);
66        }
67        else
68        {
69            return binary(nums, 0, pivot - 1, target);
70        }
71    }
72}
73