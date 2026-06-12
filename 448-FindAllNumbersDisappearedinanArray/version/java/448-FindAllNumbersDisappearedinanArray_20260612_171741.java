// Last updated: 6/12/2026, 5:17:41 PM
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
23        for(int j = 0; j <nums.length; j++)
24        {
25            if(nums[j]!=j+1)
26            {
27                a.add(j+1);
28            }
29            
30        }
31        return a;
32
33        // return new ArrayList<>();
34    }
35}