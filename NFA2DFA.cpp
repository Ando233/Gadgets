#include <bits/stdc++.h>
using namespace std;
//  全局的状态转移
map<char, map<char, set<char>>> trans;
vector<set<char>> C;

void print_set(set<int> a){
    for(auto state : a){
        cout << state << ' ';
    }
    cout << '\n';
}

bool is_existed(set<char> s){
    for(auto p : C){
        if(p == s){
            return true;
        }
    }
    return false;
}

set<char> get_episilon_closure(set<char> a){
    set<char> closure;
    queue<char> q;
    for(auto state : a){
        q.push(state);
    }
    while (!q.empty()) {
        int u = q.front(); 
        q.pop();
        closure.insert(u);
        if(trans[u].find('@') != trans[u].end()){
            for (auto v : trans[u]['@']) {
                q.push(v);
            }
        }
    }
    return closure;
}

set<char> move(set<char> a, char b){
    set<char> res;
    for(auto state : a){
        if(trans[state].find(b) != trans[state].end()){
            set<char> tmp = trans[state][b];
            for(auto state_tmp : tmp){
                res.insert(state_tmp);
            }
        }
    }

    return res;
}

int main(){
     // 读入输入
    int char_num, start_num, final_num, trans_num;
    cin >> char_num;
    vector<char> chars(char_num);
    for (int i = 0; i < char_num; i++) {
        cin >> chars[i];
    }
    cin >> start_num;
    set<char> start_states;
    for (int i = 0; i < start_num; i++) {
        char state;
        cin >> state;
        start_states.insert(state);
    }
    cin >> final_num;
    set<char> final_states;
    for (int i = 0; i < final_num; i++) {
        char state;
        cin >> state;
        final_states.insert(state);
    }
    cin >> trans_num;
    for (int i = 0; i < trans_num; i++) {
        char start, end;
        char c;
        cin >> start >> c >> end;
        trans[start][c].insert(end);
    }

    map<set<char>, int> state_idx;
    map<int, map<char, set<int>>> dfa;
    queue<set<char>> state_queue;
    int state_num = 0;

    set<char> start_closure = get_episilon_closure(start_states);

    C.push_back(start_closure);
    state_queue.push(start_closure);
    state_idx[start_closure] = state_num++;

    while (!state_queue.empty()){
        set<char> T = state_queue.front();
        state_queue.pop();

        int idx_t = state_idx[T];
        for(char a : chars){
            set<char> U = get_episilon_closure(move(T, a));
            if(U.size() == 0){
                continue;
            }
            //  U没有被标记过
            if(!is_existed(U)){
                C.push_back(U);
                state_queue.push(U);
                //  核心的DFA构建  
                dfa[idx_t][a].insert(state_num);
                //  发现新的状态，为其标号
                state_idx[U] = state_num++;
            }
            else{
                int idx_u = state_idx[U];
                dfa[idx_t][a].insert(idx_u);
            }
        }
    }
    // for (auto s : C){
    //     print_set(s);
    // }

    for(auto p : dfa){
        int from = p.first;
        for(auto pp : p.second){
            char a = pp.first;
            for(auto to : pp.second){
                cout << from << " " << a << " " << to << '\n';
            }
        }
    }

    //  找dfa的终态
    set<int> dfa_final_states;
    for(auto p : C){
        for(auto final : final_states){
            if(p.count(final)){
                int idx = state_idx[p];
                dfa_final_states.insert(idx);
            }
        }
    }

    long long unsigned int cnt = 1;
    for(auto dfa_final : dfa_final_states){
        cout << dfa_final;
        if(cnt != dfa_final_states.size()){
            cout << ' ';
        }
        cnt++;
    }

    return 0;
} 