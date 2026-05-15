class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> dict = new HashMap<>();

        for (int n : nums){
            System.out.println(dict);
            if(dict.containsKey(n)){
                return true;
            }
            dict.put(n, n);
        }
        return false;
    }
}