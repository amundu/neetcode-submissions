class TimeMap {
    public HashMap<String, ArrayList<TimeMapValue>> mp = new HashMap();

    public TimeMap() {
    }
    
    public void set(String key, String value, int timestamp) {
        mp.computeIfAbsent(key, k -> new ArrayList());
        mp.get(key).add(new TimeMapValue(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if (!mp.containsKey(key)){
            return "";
        }

        ArrayList<TimeMapValue> values = mp.get(key);
        int low = 0, high = values.size()-1;

        while (low <= high){
            int mid = low + (high - low) / 2;

            if (values.get(mid).timestamp > timestamp){
                high = mid - 1;
            } else if(values.get(mid).timestamp < timestamp){
                low = mid + 1;
            } else{
                low = mid;
                break;
            }
        }

        System.out.println(low);
        if (low == values.size()){
            return values.get(values.size()-1).timestamp < timestamp ? values.get(values.size()-1).value : "";
        }

        if (high == -1){
            return "";
        }

        if (values.get(low).timestamp > timestamp){
            while (low > 0 && values.get(low).timestamp > timestamp){
                low--;
            }
            return values.get(low).value;
        }

        while (low < values.size() && values.get(low).timestamp < timestamp){
            low++;
        }
        return values.get(low).value;
    }
}

class TimeMapValue{
    public String value;
    public int timestamp;

    public TimeMapValue(String value, int timestamp){
        this.value = value;
        this.timestamp = timestamp;
    }
}
