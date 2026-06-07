// Last updated: 6/7/2026, 7:20:51 AM
1class Solution {
2    public int peakIndexInMountainArray(int[] arr) {
3        int n = arr.length;
4        if(n==1)
5        {
6            return 0;
7        }
8        // if(arr[n-1]>arr[n-2])
9        // {
10        //     return n-1;
11        // }
12        int low=1;
13        int high = n-2;
14        
15        while(low<=high)
16        {
17            int mid=Math.floorDiv((low+high),2);
18            if(arr[mid]>arr[mid+1] && arr[mid] > arr[mid-1])
19            {
20                return mid;
21            }
22            if(arr[mid]<arr[mid+1])
23            {
24                low=mid+ 1;
25            }
26            else
27            {
28                high = mid-1;
29            }
30
31        }
32
33        return -1;
34    }
35}