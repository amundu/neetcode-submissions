class TimeMap {
    public HashMap<String, ArrayList<TimeMapValue>> mp = new HashMap();

    public TimeMap() {
    }
    
    public void set(String key, String value, int timestamp) {
        mp.computeIfAbsent(key, k -> new ArrayList()).add(new TimeMapValue(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        ArrayList<TimeMapValue> values = mp.getOrDefault(key, new ArrayList());
        int low = 0, high = values.size()-1;
        String result = "";

        while (low <= high){
            int mid = low + (high - low) / 2;

            if (values.get(mid).timestamp > timestamp){
                high = mid - 1;
            } else {
                result = values.get(mid).value;
                low = mid + 1;
            }
        }

        return result;
    }

    class TimeMapValue{
        public String value;
        public int timestamp;

        public TimeMapValue(String value, int timestamp){
            this.value = value;
            this.timestamp = timestamp;
        }
    }
}


