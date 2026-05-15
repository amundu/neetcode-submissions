class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        

        HashMap<String, List<String>> anagramGroups = new HashMap();
        for (String s: strs){
            String key = this.generateKey(s);
            if (!anagramGroups.containsKey(key)){
                anagramGroups.put(key, new ArrayList<String>());
            }
            anagramGroups.get(key).add(s);
        }
        return new ArrayList<>(anagramGroups.values());
    }

    public String generateKey(String s){ 
        int[] key = new int[26];
        for (int i = 0; i < s.length(); i++) {
            key[s.charAt(i)-'a'] += 1;
        }
        return Arrays.toString(key);
    }
}
