// Last updated: 6/12/2026, 6:13:57 PM
1class Solution {
2    public int[] findErrorNums(int[] nums) 
3    {
4        int i=0;
5        while(i<nums.length)
6        {
7            int correct =nums[i]-1;
8            if(nums[i]!=nums[correct])
9            {
10                int temp =nums[i];
11                nums[i]=nums[correct];
12                nums[correct]= temp;
13            }
14            else
15            {
16                i++;
17            }
18        }
19        for(int j = 0; j <nums.length; j++)
20        {
21            if(nums[j]-1!=j || (j+1)!=nums[j])
22            {
23                return new int[]{nums[j],j+1};
24            } 
25        }
26        return new int[]{-1,-1};
27          
28    }
29}