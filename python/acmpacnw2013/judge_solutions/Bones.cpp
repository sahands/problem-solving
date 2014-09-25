#include <iostream>
#include <vector>

#define INF 100000000000L

using namespace std;

typedef long long ll;
typedef vector<ll> VL;
typedef vector<VL> VVL;

void floyd(VVL &dist) {
  for (int i = 0; i < dist.size(); i++) dist[i][i] = 0;
  for (int k = 0; k < dist.size(); k++) {
    for (int i = 0; i < dist.size(); i++) {
      for (int j = 0; j < dist.size(); j++) {
        if (dist[i][j] > dist[i][k] + dist[k][j]) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }
}

int main() {
  int T;
  cin >> T;
  for (int tc = 0; tc < T; tc++) {
    int N, K, M;
    cin >> N >> K >> M;
    VVL dist(N, VL(N, INF));
    for (int i = 0; i < M; i++) {
      int u, v, d;
      cin >> u >> v >> d;
      dist[u][v] = dist[v][u] = d;
    }
    floyd(dist);
    ll min = 1, max = INF;
    ll ans = max;
    while (min <= max) {
      ll mid = (min + max) / 2;
      
      VVL red(N, VL(N, INF));
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          red[i][j] = dist[i][j] <= mid ? 1 : INF;
        }
      }
      floyd(red);
      ll d = 0;
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          if (red[i][j] > d) d = red[i][j];
        }
      }
      if (d <= K) {
        ans = mid;
        max = mid - 1;
      } else {
        min = mid + 1;
      }
    }
    cout << ans << endl;
  }
}
