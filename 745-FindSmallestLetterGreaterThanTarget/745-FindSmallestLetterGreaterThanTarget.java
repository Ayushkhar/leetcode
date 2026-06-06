// Last updated: 6/6/2026, 10:25:22 PM
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int low=0;
        int high =letters.length -1;
        int len =letters.length;
        
        while(low <= high)
        {
            int mid = Math.floorDiv((low + high),2);
            if(letters[mid]==target)
            {
                low=mid+1;
            }
            if(letters[mid]<target)
            {
                low = mid +1;
            }
            else
            {
                high =mid-1;
            }

        }
        for (int i = 0; i < letters.length; i++) {
            if (letters[i] > target) {
                return letters[i];  
            }
        }
        return letters[0];
    }
}