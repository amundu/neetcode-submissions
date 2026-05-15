public class Solution {
    public bool hasDuplicate(int[] nums) {
        var prev_values = new HashSet<int>();
        foreach (var num in nums){
            if (prev_values.Contains(num)){
                return true;
            }
            prev_values.Add(num);
        }
        return false;
    }
}
