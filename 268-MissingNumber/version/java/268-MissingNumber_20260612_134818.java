// Last updated: 6/12/2026, 1:48:18 PM
1class Solution {
2    public int missingNumber(int[] nums) 
3    {
4        int cnt =0;
5        for (int i = 0; i < nums.length; i++) {
6            cnt+=1;
7        }
8        for(int j = 0; j <= cnt; j++)
9{
10    boolean found = false;
11
12    for(int i = 0; i < nums.length; i++)
13    {
14        if(nums[i] == j)
15        {
16            found = true;
17            break;
18        }
19    }
20
21    if(found == false)
22    {
23        return j;
24    }
25}
26return -1;
27    }
28}