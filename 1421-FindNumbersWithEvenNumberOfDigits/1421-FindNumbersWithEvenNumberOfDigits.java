// Last updated: 6/6/2026, 10:24:54 PM
class Solution {
    public int findNumbers(int[] nums) 
    {
        int count = 0;
        for(int i = 0;i<nums.length;i++)
        {
            // String str = new 
            String str = Integer.toString(nums[i]);
            int len = str.length();
            if(len % 2 == 0)
            {
                count++;
            }
        }
        return count;
        
    }
}