#include <iostream>
#include <vector>
using namespace std ;
const int INFTY = 1000000000 ;
int main(int argc, char *argv[]) {
   int kases, n ;
   cin >> kases ;
   for (int kase=1; kase<=kases; kase++) {
      cin >> n ;
      vector<int> v(n) ;
      int min = INFTY ;
      int maxx = -INFTY ;
      for (int i=0; i<n; i++) {
         cin >> v[i] ;
         if (v[i] < min)
            min = v[i] ;
         if (v[i] > maxx)
            maxx = v[i] ;
      }
      int mid = (maxx + min) / 2 ;
      int mleft = min ;
      int mright = maxx ;
      for (int i=0; i<n; i++) {
         if (v[i] < mright && v[i] > mid)
            mright = v[i] ;
         if (v[i] > mleft && v[i] <= mid)
            mleft = v[i] ;
      }
      cout << max(mleft-min, maxx-mright) << endl ;
   }
}
