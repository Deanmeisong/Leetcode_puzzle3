class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        cnt = Counter()
        for res in responses:
            for s in set(res.split()):
                cnt[s] +=1
        
        return sorted(features, key=lambda w : -cnt[w])