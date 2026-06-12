// Last updated: 6/12/2026, 5:51:45 PM
class Solution {
    public List<Integer> findDuplicates(int[] nums) 
    {
        int i = 0;

        while(i < nums.length)
        {
            int correct = nums[i] - 1;

            if(nums[i] != nums[correct])
            {
                int temp = nums[i];
                nums[i] = nums[correct];
                nums[correct] = temp;
            }
            else
            {
                i++;
            }
        }
          
        ArrayList<Integer> a = new ArrayList<>();
        for(int j = 0; j <nums.length; j++)
        {
            // System.out.println(nums[j] + "");
            if(nums[j]-1!=j)
            {
                a.add(nums[j]);
            }
            
        }
        return a;

        
    }
}