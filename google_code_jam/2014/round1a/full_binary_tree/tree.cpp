#include <iostream>
#include <vector>
#include <algorithm>

#define M 1001

using namespace std;

void try_root(int N, vector<int> *G, int r, int parent, int &s, int &c) {
    int child_count = 0;
    int not_parent = -1;
    for(int i =0; i < G[r].size(); i++) {
        if(G[r][i] != parent) {
            child_count ++;
            not_parent = i;
        }
    }

    // cout << r << " has " << child_count << " children" << endl;

    if (child_count == 1){
        int sc = 0, cc = 0;
        try_root(N, G, G[r][not_parent], r, sc, cc);
        s = cc;
        c = cc + 1;
        // cout << "One child only " << r << endl;
    } else if(child_count == 0 || child_count == 2) {
        s=0;
        c=1;
        for(int i =0; i < G[r].size(); i++) {
            if(G[r][i] != parent) {
                int sc = 0, cc = 0;
                try_root(N, G, G[r][i], r, sc, cc);
                s += sc;
                c += cc;
            }
        }
        // cout << " Subreee " << r << " needs " << s << " removed" << endl;
    } else {
        // > 2
        vector<int> SS;
        vector<int> SC;
        for(int i =0; i < G[r].size(); i++) {
            if(G[r][i] != parent) {
                int sc = 0, cc = 0;
                try_root(N, G, G[r][i], r, sc, cc);
                SS.push_back(sc);
                SC.push_back(cc);
            }
        }

        // for(int i =0; i < SS.size(); i++) {
        //         cout << SS[i] << " " << SC[i] << "; ";
        // }
        // cout << endl;

        int largest1 = 0, largest2 = 1;
        if(SC[0] - SS[0] < SC[1] - SS[1]) {
            largest1 = 1, largest2 = 0;
        }

        for(int i =2; i < SS.size(); i++) {
            if(SC[i] - SS[i] > SC[largest1] - SS[largest1]) {
                largest2 = largest1;
                largest1 = i;
            } else if(SC[i] - SS[i] > SC[largest2] - SS[largest2]) {
                largest2 = i;
            }
        }


        // cout << "    Largest1 " << largest1 << "   LArgest2 " << largest2 << endl;

        c = SC[largest1] + SC[largest2];
        s = SS[largest1] + SS[largest2];
        for(int i =0; i < SS.size(); i++) {
            if(i != largest1 && i !=largest2) {
                c+= SC[i];
                s += SC[i];
            }
        }
    }
}

int solve(int N, vector<int> *G) {
    int best = M;
    for(int r = 1; r <= N; r++ ) {
        int s =0, c= 0;
        cout << "Trying " << r << endl;
        try_root(N, G, r, -1, s, c);
        cout << "Need to remove " << s << " nodes, " << c << " nodes total." << endl;
        best = min(best, s);
    }
    return best;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        vector<int> G[M];
        for(int i =0; i < N - 1; i ++) {
            int u, v;
            cin >> u >> v;
            G[u].push_back(v);
            G[v].push_back(u);
        }
        int best = solve(N, G);
        cout << "Case #" << t << ": " << best << endl;
    }
}

