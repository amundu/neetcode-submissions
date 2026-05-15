class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length){
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int total = nums1.length + nums2.length;
        int half = (total + 1) / 2;

        int l = 0, r = nums1.length;  // ✓ Search over counts, not indices

        while (l <= r) {
            int mid = l + (r-l)/ 2;  // mid = count of elements from nums1
            int j = half - mid;      // j = count of elements from nums2
            
            // Convert counts to indices for boundary access
            int aLeft = mid > 0 ? nums1[mid - 1] : Integer.MIN_VALUE;
            int aRight = mid < nums1.length ? nums1[mid] : Integer.MAX_VALUE;
            int bLeft = j > 0 ? nums2[j - 1] : Integer.MIN_VALUE;
            int bRight = j < nums2.length ? nums2[j] : Integer.MAX_VALUE;
            
            if (aLeft <= bRight && bLeft <= aRight) {
                if (total % 2 != 0) {
                    return Math.max(aLeft, bLeft);  // odd: max of lefts
                }
                return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2.0;
            } else if (aLeft > bRight) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }
}
