class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet();

        int l = 0;
        int maxLength = 0;
        for (int r = 0; r < s.length(); r++){
            char currChar = s.charAt(r);
            while (set.contains(currChar)){
                set.remove(s.charAt(l));
                l++;
            }
            set.add(currChar);
            maxLength = Math.max(maxLength, set.size());
        }
        return maxLength;
    }
}
