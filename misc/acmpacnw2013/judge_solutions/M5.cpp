#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

const int INF = 1000000000;

struct MinCostMaxFlow {
  int N;
  VVI cap, flow, cost;
  VI found, dad, dist, pi;  

  bool search(int source, int sink) {
    fill(found.begin(), found.end(), false);
    fill(dist.begin(), dist.end(), INF);
    dist[source] = 0;

    while (source != N) {
      int best = N;
      found[source] = true;
      for (int k = 0; k < N; k++) {
	if (found[k]) continue;
        if (flow[k][source]) {
          int val = dist[source] + pi[source] - pi[k] - cost[k][source];
          if (dist[k] > val) {
            dist[k] = val;
            dad[k] = source;
          }
        }
	if (flow[source][k] < cap[source][k]) {
          int val = dist[source] + pi[source] - pi[k] + cost[source][k];
          if (dist[k] > val) {
            dist[k] = val;
            dad[k] = source;
          }
	}

        if (dist[k] < dist[best]) best = k;
      }
      source = best;
    }
    for (int k = 0; k < N; k++)
      pi[k] = min(pi[k] + dist[k], INF);
    return found[sink];
  }
    
  pair<int,int> getMaxFlow(const VVI &cap, const VVI &cost, int source, int sink) {
    this->cap = cap;
    this->cost = cost;

    N = cap.size();
    found = VI(N);
    flow = VVI(N,VI(N));
    dist = VI(N+1);
    dad = VI(N);
    pi = VI(N);

    int totflow = 0, totcost = 0;
    while (search(source, sink)) {
      int amt = INF;
      for (int x = sink; x != source; x = dad[x])
        amt = min(amt, flow[x][dad[x]] ? flow[x][dad[x]] :
                  cap[dad[x]][x] - flow[dad[x]][x]);
      for (int x = sink; x != source; x = dad[x]) {
	if (flow[x][dad[x]]) {
	  flow[x][dad[x]] -= amt;
	  totcost -= amt * cost[x][dad[x]];
	} else {
	  flow[dad[x]][x] += amt;
	  totcost += amt * cost[dad[x]][x];
	}
      }
      totflow += amt;
    }
    
    return make_pair(totflow, totcost);
  }
};

int main() {
  int T;
  cin >> T;
  for (int tc = 0; tc < T; tc++) {
  
    int M, N, A, B;
    cin >> M >> N >> A >> B;
    VI Acomp(N), Bcomp(N);
    for (int i = 0; i < N; i++) cin >> Acomp[i];
    for (int i = 0; i < N; i++) cin >> Bcomp[i];
    VVI mat(M, VI(N));
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        cin >> mat[i][j];
      }
    }
    
    int nv = 2 * N + M + 2;
    VVI cap(nv, VI(nv)), cost(nv, VI(nv));
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        cap[i][N+j] = cap[N+j][M+N+i] = 100;
        cost[i][N+j] = A * mat[j][i];
        cost[N+j][M+N+i] = B * mat[j][i];
      }
      cap[nv-2][i] = Acomp[i];
      cap[M+N+i][nv-1] = Bcomp[i];
    }
    
    MinCostMaxFlow flow;
    pair<int, int> ans = flow.getMaxFlow(cap, cost, nv-2, nv-1);
    cout << ans.second << endl;
  }
}

