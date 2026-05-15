class Solution {
    public int findMin(int[] nums) {
        int low = 0, high = nums.length-1;

        while (low <= high){
            if (nums[low] <= nums[high]){
                return nums[low];
            }

            int mid = ((high-low)/2)+low;
            if (nums[low] <= nums[mid]){
                low = mid + 1;
            }else{
                high = mid;
            }
        }
        return nums[low];
    }
}
