class TimeMap {
    private Map<String, ArrayList<Pair<Integer, String>>> mp;

    public TimeMap() {
        mp = new HashMap();
    }
    
    public void set(String key, String value, int timestamp) {
        mp.computeIfAbsent(key, k -> new ArrayList()).add(new Pair(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        ArrayList<Pair<Integer, String>> values = mp.getOrDefault(key, new ArrayList());
        int low = 0, high = values.size()-1;
        String result = "";

        while (low <= high){
            int mid = low + (high - low) / 2;

            if (values.get(mid).getKey() > timestamp){
                high = mid - 1;
            } else {
                result = values.get(mid).getValue();
                low = mid + 1;
            }
        }

        return result;
    }

    private static class Pair<K, V>{
        private final K key;
        private final V value;

        public Pair(K key, V value){
            this.key = key;
            this.value = value;
        }

        public K getKey(){
            return key;
        }

        public V getValue(){
            return value;
        }
    }
}


