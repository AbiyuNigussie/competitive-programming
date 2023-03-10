#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> res;
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = 0; j < nums.size(); j++)
            {

                if (nums[i] + nums[j] == target and res.size() < 2)
                {
                    if (i == j)
                        continue;
                    res.push_back(i);
                    res.push_back(j);
                }
            }
        }
        return res;
    }
};
