class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length){
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        int l = 0, r = nums1.length; 
        int n = nums1.length + nums2.length;
        int half = (n+1)/2;
        while (l <= r){
            int mid = l + (r - l)/2;
            int j = half - mid;

            int aLeft = mid > 0 ? nums1[mid-1] : Integer.MIN_VALUE;
            int aRight = mid  < nums1.length ? nums1[mid] : Integer.MAX_VALUE;
            int bLeft = j > 0 ? nums2[j-1] : Integer.MIN_VALUE;
            int bRight = j < nums2.length ? nums2[j] : Integer.MAX_VALUE;
            System.out.printf("%d %d\n", l ,r);
            if (aLeft <= bRight && bLeft <= aRight){
                if (n % 2 != 0){
                    return Math.max(aLeft, bLeft);
                }
                return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight))/2.0;
            }else if (aLeft > bRight){
                r = mid -1;
            }else{
                l = mid + 1;
            }
        }
        return -1;
    }
}
