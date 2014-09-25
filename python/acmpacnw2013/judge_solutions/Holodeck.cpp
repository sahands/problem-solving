#include <iostream>
using namespace std ;
typedef long long ll ;
int mabs(int v) {
   return v < 0 ? -v : v ;
}
ll cnt(ll v, ll d, int isfirst) {
   if (d == 0 && v == 0)
      return 1 ;
   if (v < 0 || v >= d * 20)
      return 0 ;
   if (d == 1) {
      if ((v & 1) == 0)
         return 1 ;
      else
         return 0 ;
   }
   ll r = 0 ;
   for (int p=v%10; p<20; p+=10) {
      r += ((10-mabs(p-9)) - isfirst) * cnt((v - p*d - p) / 10, d/100, 0) ;
      isfirst = 0 ;
   }
   return r ;
}
ll cnt(ll v) {
   ll r = 0 ;
   for (ll d=1; d<=v+1; d *= 10)
      r += cnt(v, d, 1) ;
   return r ;
}
int main(int argc, char *argv[]) {
   int kases ;
   cin >> kases ;
   for (int kase=1; kase<=kases; kase++) {
      ll v ;
      cin >> v ;
      if (v < 0)
         break ;
      cout << cnt(v) << endl ;
   }
}
