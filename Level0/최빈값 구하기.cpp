#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    
    // array 내에서 각 수의 수를 세기
    int count[1001] = {0, };
    for(int i = 0; i < array.size(); i++)
        count[array[i]]++;
    
    // 최빈값 = max_val, 최빈값이 나타난 idx = max_idx
    int max_val = -1, max_idx = 0;
    for(int i = 0; i < 1001; i++)
        if(max_val < count[i]) {
            max_val = count[i];
            max_idx = i;
        }
    
    // 최빈값이 여러 개인지 판별
    int max_cnt = 0;
    for(int i = 0; i < 1001; i++)
        if(count[i] == max_val) max_cnt++;
    return max_cnt > 1 ? -1 : max_idx;
}
