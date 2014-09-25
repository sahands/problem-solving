#include <iostream>
using namespace std ;
int main(int argc, char *argv[]) {
   int kases ;
   cin >> kases ;
   for (int kase=1; kase<=kases; kase++) {
      int N, D ;
      cin >> N >> D ;
      int r = 0 ;
      for (int i=0; i<N; i++) {
         int vi, fi, ci ;
         cin >> vi >> fi >> ci ;
         if (vi * fi >= D * ci)
            r++ ;
      }
      cout << r << endl ;
   }
}
