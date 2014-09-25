#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;

int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, -1, 0, 1};

struct loc {
  int r, c, d;
  bool operator<(const loc &o) const {
    return d > o.d;
  }
};

int main() {
  int T;
  cin >> T;
  VI delay(26);
  for (int tc = 0; tc < T; tc++) {
    int k, w, h;
    cin >> k >> w >> h;
    char c;
    int d;
    for (int i = 0; i < k; i++) {
      cin >> c >> d;
      delay[c - 'A'] = d;
    }
    
    VVI dist(h, VI(w));
    loc start;
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
        cin >> c;
        dist[i][j] = delay[c - 'A'];
        if (c == 'E') {
          start.r = i;
          start.c = j;
          start.d = 0;
        }
      }
    }
    
    VVB visited(h, VB(w));
    
    priority_queue<loc> pq;
    pq.push(start);
    while (!pq.empty()) {
      loc cur = pq.top();
      pq.pop();
      if (visited[cur.r][cur.c]) continue;
      visited[cur.r][cur.c] = true;
      if (cur.r == 0 || cur.r == h - 1 || cur.c == 0 || cur.c == w - 1) {
        cout << cur.d << endl;
        break;
      }
      for (int i = 0; i < 4; i++) {
        loc next;
        next.r = cur.r + dr[i];
        next.c = cur.c + dc[i];
        next.d = cur.d + dist[next.r][next.c];
        if (!visited[next.r][next.c]) pq.push(next);
      }
    }
  }
}
