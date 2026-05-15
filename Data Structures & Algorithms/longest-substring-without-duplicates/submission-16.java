class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> mp = new HashMap();

        int l = 0;
        int maxLength = 0;
        for (int r = 0; r < s.length(); r++){
            char currChar = s.charAt(r);
            if (mp.containsKey(currChar)){
                l = Math.max(mp.get(currChar)+1, l);
            }
            mp.put(currChar, r);
            maxLength = Math.max(maxLength, r-l+1);
        }
        return maxLength;
    }
}
