class Solution {
    public int longestWPI(int[] hours) {
        int ans = 0, s = 0;
        Map<Integer,Integer> presum = new HashMap<>();
        for(int i = 0; i < hours.length; ++i) {
            s += hours[i] > 8 ? 1 : -1;
            if(s > 0) ans = i+1;
            else if(presum.containsKey(s-1)) ans = Math.max(ans, i-presum.get(s - 1));
            if(!presum.containsKey(s)) presum.put(s,i);
        }
        return ans;
    }
}