class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String word: strs){
            sb.append(word.length()).append('#').append(word);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        int l = 0;
        int r = 0;
        List<String> output = new ArrayList();
        System.out.println(str);
        while (r < str.length()){
            if (str.charAt(r) != '#'){
                r++;
                continue;
            }
            System.out.println(l + " " + r);
            int n = Integer.parseInt(str.substring(l, r));
            l = ++r;
            r += n;
            String word = str.substring(l, r);
            output.add(word);
            l = r;
        }
        return output;
    }
}
