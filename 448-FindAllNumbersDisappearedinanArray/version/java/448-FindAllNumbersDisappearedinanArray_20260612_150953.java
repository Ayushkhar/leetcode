// Last updated: 6/12/2026, 3:09:53 PM
1class Solution {
2
3    public List<Integer> findDisappearedNumbers(int[] nums) 
4    {
5        int i = 0;
6
7        while(i < nums.length)
8        {
9            int correct = nums[i] - 1;
10
11            if(nums[i] != nums[correct])
12            {
13                int temp = nums[i];
14                nums[i] = nums[correct];
15                nums[correct] = temp;
16            }
17            else
18            {
19                i++;
20            }
21        }
22        ArrayList<Integer> a = new ArrayList<>();
23
24        for(int j = 0; j <nums.length; j++)
25        {
26            // System.out.println(nums[j]);
27            if(nums[j]!=j+1)
28            {
29                a.add(j+1);
30            }
31        }
32        return a;
33
34        // return new ArrayList<>();
35    }
36}