// Last updated: 6/6/2026, 10:24:42 PM
class Solution {
    public int maximumWealth(int[][] accounts) 
    {
        int[] arr = new int[accounts.length];
        for(int i = 0;i<accounts.length;i++)
        {
            int suma = 0;
            for(int j= 0;j<accounts[i].length;j++)
            {
                
                suma+=accounts[i][j];

            }
            arr[i] = suma;
        }
        int max=0;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]>max)
            {
                max=arr[i];

            }
        }
        return max;
    }
}