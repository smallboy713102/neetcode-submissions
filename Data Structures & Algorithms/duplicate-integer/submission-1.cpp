class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int>mp;
        bool flag = false;
        for(int x: nums){
            if (mp[x]==0){
                mp[x]=1;
            }
            else{
                flag = true;
                break;
            }
        }
        return flag;
    }
};
