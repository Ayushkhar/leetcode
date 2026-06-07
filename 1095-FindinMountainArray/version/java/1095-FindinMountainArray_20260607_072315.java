// Last updated: 6/7/2026, 7:23:15 AM
1class Solution
2{
3    public int findInMountainArray(int target, MountainArray mountainArr)
4    {
5        int peakIndex = peak(mountainArr);
6
7        // search in ascending part
8        int first = binarySearch(
9            mountainArr,
10            target,
11            0,
12            peakIndex,
13            true
14        );
15
16        if (first != -1)
17        {
18            return first;
19        }
20
21        // search in descending part
22        return binarySearch(
23            mountainArr,
24            target,
25            peakIndex + 1,
26            mountainArr.length() - 1,
27            false
28        );
29    }
30
31    int peak(MountainArray mountainArr)
32    {
33        int low = 0;
34        int high = mountainArr.length() - 1;
35
36        while (low < high)
37        {
38            int mid = (low + high) / 2;
39
40            if (mountainArr.get(mid) < mountainArr.get(mid + 1))
41            {
42                low = mid + 1;
43            }
44            else
45            {
46                high = mid;
47            }
48        }
49
50        return low;
51    }
52
53    int binarySearch(
54        MountainArray mountainArr,
55        int target,
56        int low,
57        int high,
58        boolean asc
59    )
60    {
61        while (low <= high)
62        {
63            int mid = (low + high) / 2;
64
65            int value = mountainArr.get(mid);
66
67            if (value == target)
68            {
69                return mid;
70            }
71
72            if (asc)
73            {
74                if (value < target)
75                {
76                    low = mid + 1;
77                }
78                else
79                {
80                    high = mid - 1;
81                }
82            }
83            else
84            {
85                if (value < target)
86                {
87                    high = mid - 1;
88                }
89                else
90                {
91                    low = mid + 1;
92                }
93            }
94        }
95
96        return -1;
97    }
98}