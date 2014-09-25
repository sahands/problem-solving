#include <iostream>
#include <cstring>
using namespace std ;
typedef unsigned long long ull ;
const int P = 193 ; // a moderate prime
const int BINMIL = 1024 * 1024 ;
struct node {
   char label, src ;
   int size ;
   ull hash ;
   struct node *parent, *progeny, *sib, *hashnext, *canon ;
} nodes[BINMIL], *hashtab[BINMIL] ;
int at = 0 ;
int hival ;
int nodeeq(node *a, node *b) {
   if (a == b || a->canon == b->canon)
      return 1 ;
   if (a->hash != b->hash)
      return 0 ;
   if (a->label != b->label)
      return 0 ;
   node *p1 = a->progeny ;
   node *p2 = b->progeny ;
   while (p1 && p2) {
      if (!nodeeq(p1, p2))
         return 0 ;
      p1 = p1->sib ;
      p2 = p2->sib ;
   }
   if (p1 || p2)
      return 0 ;
   b->canon = a ;
   return 1 ;
}
node *rehash(node *n) {
   ull r = n->label ;
   for (node *p=n->progeny; p; p=p->sib) {
      r = r * P + rehash(p)->hash ;
      n->size += p->size ;
   }
   n->hash = r ;
   int h = (int)(r & (BINMIL-1)) ;
   for (node *p=hashtab[h]; p; p=p->hashnext)
      if (nodeeq(p, n)) {
         if (n->src != p->src && n->size > hival)
            hival = n->size ;
         n->canon = p ;
         return n ;
      }
   n->hashnext = hashtab[h] ;
   hashtab[h] = n ;
   n->canon = n ;
   return n ;
}
void readtree(int sz, char src) {
   char c ;
   int p, base=at ;
   node *root ;
   for (int i=0; i<sz; i++) {
      cin >> c >> p ;
      node *n = nodes + at++ ;
      n->label = c ;
      n->size = 1 ;
      n->src = src ;
      if (p >= 0) {
         n->parent = nodes + base + p ;
         n->sib = n->parent->progeny ;
         n->parent->progeny = n ;
      } else {
         root = n ;
      }
   }
   rehash(root) ;
}
void doone() {
   int M, N ;
   cin >> M >> N ;
   memset(nodes, 0, (M+N)*sizeof(struct node)) ;
   memset(hashtab, 0, sizeof(hashtab)) ;
   hival = 0 ;
   readtree(M, 'a') ;
   readtree(N, 'b') ;
   cout << hival << endl ;
}
int main(int argc, char *argv[]) {
   int kases ;
   cin >> kases ;
   for (int kase=1; kase<=kases; kase++)
      doone() ;
}
