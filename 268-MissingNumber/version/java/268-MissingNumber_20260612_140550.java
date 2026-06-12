// Last updated: 6/12/2026, 2:05:50 PM
1class Solution {
2    public int missingNumber(int[] nums) 
3    {
4        int i=0;
5        while(i<nums.length)
6        {
7            int correct =nums[i];
8            if(nums[i]<nums.length && nums[i]!=nums[correct])
9            {
10                int temp =nums[i];
11                nums[i]=nums[correct];
12                nums[correct] =temp;
13            }
14            else
15            {
16                i++;
17            }
18        }
19        for(int j=0;j<nums.length;j++)
20        {
21            if(nums[j]!=j)
22            {
23                return j;
24                // break;
25            }
26        }
27        return nums.length;
28    }
29}