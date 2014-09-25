// Solution to Tribbles by jcd.

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define fr(x,y,z) for((x)=(y);(x)<(z);(x)++)

#define MAX_CASES 69
#define MAX_N 67

unsigned long long f[MAX_N+1];

int main(void) {
  int i,ncas;
  assert(scanf("%d",&ncas)==1);
  assert(ncas <= MAX_CASES);
  f[0]=1;
  f[1]=1;
  f[2]=2;
  f[3]=4;
  fr(i,4,MAX_N+1) f[i]=f[i-1]+f[i-2]+f[i-3]+f[i-4];

  for(int cas=1;cas<=ncas;cas++) {
    int n;
    assert(scanf("%d",&n)==1);
    assert(n>=0); assert(n<=MAX_N);
    printf("%llu\n",f[n]);
  }

  return 0;
}

