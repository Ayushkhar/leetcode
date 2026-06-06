// Last updated: 6/6/2026, 10:26:59 PM
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target)
{
        int row = matrixSize;
        int col = matrixColSize[0];

        int low = 0;
        int high = row*col -1;

        while(low<=high)
        {
            int mid = (low+high)/2;
            int r = mid / col;
            int c = mid % col;

            if(matrix[r][c] == target)
            {
                return true;
            }
            else if(matrix[r][c]<target)
            {
                low = mid+1;
            }
            else
            {
                high = mid-1;
            }

        }
        return false;

}