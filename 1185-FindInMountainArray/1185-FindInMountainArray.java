// Last updated: 6/7/2026, 7:09:46 PM
class Solution
{
    public int findInMountainArray(int target, MountainArray mountainArr)
    {
        int peakIndex = peak(mountainArr);

        // search in ascending part
        int first = binarySearch(
            mountainArr,
            target,
            0,
            peakIndex,
            true
        );

        if (first != -1)
        {
            return first;
        }

        // search in descending part
        return binarySearch(
            mountainArr,
            target,
            peakIndex + 1,
            mountainArr.length() - 1,
            false
        );
    }

    int peak(MountainArray mountainArr)
    {
        int low = 0;
        int high = mountainArr.length() - 1;

        while (low < high)
        {
            int mid = (low + high) / 2;

            if (mountainArr.get(mid) < mountainArr.get(mid + 1))
            {
                low = mid + 1;
            }
            else
            {
                high = mid;
            }
        }

        return low;
    }

    int binarySearch(
        MountainArray mountainArr,
        int target,
        int low,
        int high,
        boolean asc
    )
    {
        while (low <= high)
        {
            int mid = (low + high) / 2;

            int value = mountainArr.get(mid);

            if (value == target)
            {
                return mid;
            }

            if (asc)
            {
                if (value < target)
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid - 1;
                }
            }
            else
            {
                if (value < target)
                {
                    high = mid - 1;
                }
                else
                {
                    low = mid + 1;
                }
            }
        }

        return -1;
    }
}