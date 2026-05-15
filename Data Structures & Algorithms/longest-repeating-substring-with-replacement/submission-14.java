class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0, maxFreq = 0, maxLength = 0;
        HashMap<Character, Integer> mp = new HashMap();

        for (int r = 0; r < s.length(); r++){
            mp.put(s.charAt(r), mp.getOrDefault(s.charAt(r), 0) + 1);
            int freq = mp.get(s.charAt(r));
            
            maxFreq = Math.max(maxFreq, freq);
            while (r-l-maxFreq+1 > k) {
                mp.put(s.charAt(l), mp.get(s.charAt(l))-1);
                l++;
            }
            maxLength = Math.max(maxLength, r-l+1);
        }
        return maxLength;
    }
}
