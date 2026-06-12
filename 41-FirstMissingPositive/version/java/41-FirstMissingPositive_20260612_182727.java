// Last updated: 6/12/2026, 6:27:27 PM
1class Solution {
2    public int firstMissingPositive(int[] nums) 
3    {
4        int i=0;
5        while(i<nums.length)
6        {
7            int correct = nums[i]-1;
8            if(nums[i] > 0 &&
9               nums[i] <= nums.length &&
10               nums[i] != nums[correct])
11            {
12                int temp =nums[i];
13                nums[i]=nums[correct];
14                nums[correct]=temp;
15            }
16            else
17            {
18                i++;
19            }
20        }   
21        for(int j = 0; j <nums.length; j++)
22        {
23            if(nums[j]!=j+1)
24            {
25                return j+1;
26            }
27            
28        }
29        return nums.length+1;
30    }
31     
32}