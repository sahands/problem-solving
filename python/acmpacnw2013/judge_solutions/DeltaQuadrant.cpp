#include <iostream>
#include <vector>
using namespace std ;
typedef long long ll ;
int cookie = 1001 ;
struct edge ;
struct node {
   node() : edges(), savings(), visited(0) {}
   vector<edge*> edges ;
   vector<ll> savings ;
   int visited ;
} ;
struct edge {
   edge(node *src_, node *dst_, int w_) :
       src(src_), dst(dst_), w(w_), visited(0) {
      src->edges.push_back(this) ;
      dst->edges.push_back(this) ;
   }
   node *otherend(node *n) {
      return (n == src ? dst : src) ;
   }
   node *src, *dst ;
   ll w ;
   int visited ;
} ;
void combine(vector<ll> &a, const vector<ll> &b) {
   for (int i=a.size()-1; i>=0; i--)
      for (int j=0; j<b.size() && j+i<a.size(); j++)
         a[i+j] = max(a[i+j], a[i]+b[j]) ;
}
void orient_edges(node *n) {
   for (int i=0; i<n->edges.size(); i++) {
      edge *e = n->edges[i] ;
      if (e->visited != cookie) {
         if (e->src != n)
            swap(e->src, e->dst) ;
         e->visited = cookie ;
         orient_edges(e->dst) ;
      }
   }
}
int calculate_tree_savings(node *node, int n, int k, ll weight, ll &bestval,
                           ll &edgesum) {
   int r = 1 ;
   vector<ll> &w = node->savings ;
   w.resize(k+1) ;
   edgesum = 0 ;
   for (int i=0; i<node->edges.size(); i++) {
      edge *e = node->edges[i] ;
      if (e->src == node) {
         ll thisedgesum = 0 ;
         int nc = calculate_tree_savings(e->dst, n, k, e->w, bestval,
                                         thisedgesum) ;
         if (nc >= n-k) {
            ll t = 2 * (thisedgesum - e->w) - e->dst->savings[nc-n+k] ;
            if (t < bestval)
               bestval = t ;
         }
         edgesum += thisedgesum ;
         r += nc ;
         combine(w, e->dst->savings) ;
      }
   }
   for (int i=r; i<=k; i++)
      w[i] += 2*weight ;
   edgesum += weight ;
   return r ;
}
void doone() {
   int n, k ;
   cin >> n >> k ;
   vector<node> nodes(n) ;
   ll sew = 0 ;
   for (int i=1; i<n; i++) {
      int src, dst ;
      ll w ;
      cin >> src >> dst >> w ;
      new edge(&nodes[src], &nodes[dst], w) ;
      sew += w ;
   }
   ll bestval = 2 * sew ;
   cookie++ ;
   orient_edges(&nodes[0]) ;
   ll dmy ;
   calculate_tree_savings(&nodes[0], n, k, 0, bestval, dmy) ;
   if (2 * sew - nodes[0].savings[k] < bestval)
      bestval = 2 * sew - nodes[0].savings[k] ;
   cout << bestval << endl ;
}
int main(int argc, char *argv[]) {
   int kases ;
   cin >> kases ;
   for (int kase=1; kase<=kases; kase++)
      doone() ;
}
