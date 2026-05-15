class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numsSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        System.out.println(numsSet);

        int longestSeq = 0;
        for (int n: numsSet){
            if (numsSet.contains(n-1)){
                continue;
            }
            int length = 1;
            while (numsSet.contains(n + length)){
                length++;
            }
            longestSeq = Math.max(longestSeq, length);
        }
        return longestSeq;
        
    }
}
