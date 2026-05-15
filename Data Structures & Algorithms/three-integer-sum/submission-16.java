class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> output = new ArrayList();
        for (int i = 0; i < nums.length; i++){
            if (i > 0 && nums[i-1] == nums[i]){
                continue;
            }
            int l = i+1, r = nums.length-1;
            while(l < r){
                int currSum = nums[i] + nums[l] + nums[r];
                if (currSum > 0) {
                    r--;
                } else if (currSum < 0){
                    l++;
                }else {
                    output.add(new ArrayList(Arrays.asList(nums[i], nums[l], nums[r])));
                    l++;
                    while (l<r && nums[l-1] == nums[l]){
                        l++;
                    }
                }
            }
        }

        return output;
    }
}
