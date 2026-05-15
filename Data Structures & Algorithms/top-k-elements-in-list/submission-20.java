class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freqsCounter = new HashMap();
        for (int n: nums){
            freqsCounter.merge(n, 1, Integer::sum);
        }
        int[] output = new int[k];
        List<List<Integer>> freqs = new ArrayList(nums.length+1);
        for (int i = 0; i <= nums.length; i++) {
            freqs.add(new ArrayList<>());
        }

        for (Map.Entry<Integer, Integer> entry: freqsCounter.entrySet()){
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            freqs.get(value).add(key);
        }


        for (int i = freqs.size()-1; i > 0; i--) {
            for (int j = 0; j < freqs.get(i).size(); j++){
                output[--k] = freqs.get(i).get(j);
                if (k == 0){
                    return output;
                }
            }
            
        }
        return output;
    }
}
