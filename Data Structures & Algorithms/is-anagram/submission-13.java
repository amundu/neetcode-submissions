class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] counterS = new int[26];
        int[] counterT = new int[26];

        for (int i = 0; i < s.length(); i++){
            counterS[(int)s.charAt(i) - (int)'a'] += 1;
            counterT[(int)t.charAt(i) - (int)'a'] += 1;
        }

        for (int i = 0; i < counterS.length; i++){
            if (counterS[i] != counterT[i]){
                return false;
            }
        }

        return true;
    }
}
