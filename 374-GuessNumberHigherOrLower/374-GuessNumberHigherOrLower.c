// Last updated: 6/6/2026, 10:25:46 PM
int guessNumber(int n)
{
    
    long int low, mid, high;
 
    low = 0;
    high = n;
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (guess(mid) == 0)
        {
            return mid;
        }
        else if (guess(mid)==1)
        {
            low = mid + 1;
        }
        else if(guess(mid)==-1)
        {
            high = mid - 1;
        }
    }
    return -1;
	
}