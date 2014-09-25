// Solution to MontySort by jcd.

#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

#define V(x) vector<x >
#define vs V(string)
#define vi V(int)
#define vvi V(V(int) )
#define vd V(double)

#define fr(x,y,z) for((x)=(y);(x)<(z);(x)++)
#define fo(x,y) fr(x,0,y)
#define fir(n) fo(i,n)
#define fjr(n) fo(j,n)
#define fkr(n) fo(k,n)
#define fi fir(n)
#define fj fjr(n)
#define fk fkr(n)

#define pb push_back
#define sz size()
#define mp(x,y) make_pair((x),(y))
#define df long double

int inversions(const vi& f) { int i,j,ret=0; fir(f.sz) fjr(i) if(f[j]>f[i]) ret++; return ret; }

#ifdef ALGORITHM_MONTY
while (!sorted(a)) {
  int i = random(n) ;
  int j = random(n) ;
  if (a[min(i,j)] > a[max(i,j)]) swap(a[i], a[j]) ;
}
#endif

#ifdef ALGORITHM_CARLOS
while (!sorted(a)) {
  int i = random(n-1) ;
  int j = i + 1 ;
  if (a[min(i,j)] > a[max(i,j)]) swap(a[i], a[j]) ;
}
#endif

// Do 10^5 simulations and return the average.
df montecarlo(int n, bool use_monty, const vi& ff) {
  int i,j;
  int ans=0;

  for(int iter=0;iter<100000;iter++) {
    vi perm = ff;
    while(1) {
      fr(i,1,n) if (perm[i-1]>perm[i]) break;
      if (i==n) break;
      ans++;
      if (use_monty) {
        i = random()%n;
        j = random()%n;
        if (perm[min(i,j)] > perm[max(i,j)]) swap(perm[i], perm[j]);
      } else {
        i = rand()%(n-1);
        j = i+1;
        if (perm[min(i,j)] > perm[max(i,j)]) swap(perm[i], perm[j]);
      }
    }
  }
  return ans/100000.0;
}

// Dynamic programming algorithm that computes the probability of the array
// being in each state, after 0,1,... iterations.
// Stops when the probability the array is not sorted yet becomes very small.
df slow(int n, bool use_monty, const vi& ff) {
  int i,j;
  df ans=0.0;
  map<vi,df> f,g;
  vi perm = ff;
  f[perm] = 1.0;
  df leftover = 1.0;

  for (int iter=0;;iter++) {
    perm = ff;
    sort(perm.begin(),perm.end());
    ans += f[perm] * iter;
    leftover -= f[perm];
    long double est = use_monty ? n*n : n-1;
    if (leftover * (iter+3*est) < max(1e-9 * ans, static_cast<long double>(1e-9))) {
      ans += leftover * (iter+est);
      break;
    }
    f[perm]=0.0;
    g.clear();
    leftover=0.0;
    for(map<vi,df>::const_iterator it=f.begin();it!=f.end();++it) {
      perm=it->first;
      leftover += it->second;
      if (use_monty) {
        df c = it->second / (n*n);
        fi fj {
          bool do_swap = perm[min(i,j)] > perm[max(i,j)];
          if (do_swap) swap(perm[i],perm[j]);
          g[perm] += c;
          if (do_swap) swap(perm[i],perm[j]);
        }
      } else {
        df c = it->second / (n-1);
        fir(n-1) {
          j=i+1;
          bool do_swap = perm[min(i,j)] > perm[max(i,j)];
          if (do_swap) swap(perm[i],perm[j]);
          g[perm] += c;
          if (do_swap) swap(perm[i],perm[j]);
        }
      }
    }

    f.swap(g);
  }
  return ans;
}

// Dynamic programming algorithm that computes the expected number of iterations
// required from each permutation.
// Processes permutations in order of inversion count, so there are no "loops"
// in the DP, since inversion count can only decrease in Monty's and Carlo's
// algorithms.
df fast(int n, bool use_monty, const vi& ff) {
  int i,j,k;

  // Initialize array of permutations, sorted by #inversions.
  vector<pair<int,vi> > o;
  vi perm = ff;
  sort(perm.begin(), perm.end());
  do {
    o.pb(mp(inversions(perm),perm));
  } while(next_permutation(perm.begin(),perm.end()));
  sort(o.begin(),o.end());

  // Compute expected number of iterations;
  map<vi,df> f;
  fkr(o.sz) {
    perm=o[k].second;
    if (o[k].first==0) { f[perm]=0; continue; }
    int num_noswap=0,num_swap=0;
    df ans=0.0;

    if (use_monty) {
      fi fj {
        bool do_swap = perm[min(i,j)] > perm[max(i,j)];
        if (do_swap) {
          num_swap++;
          swap(perm[i],perm[j]);
          ans += f[perm];
          swap(perm[i],perm[j]);
        } else {
          num_noswap++;
        }
      }
      f[perm]=(ans+n*n)/num_swap;
    } else {
      fir(n-1) {
        j=i+1;
        bool do_swap = perm[min(i,j)] > perm[max(i,j)];
        if (do_swap) {
          num_swap++;
          swap(perm[i],perm[j]);
          ans += f[perm];
          swap(perm[i],perm[j]);
        } else {
          num_noswap++;
        }
      }
      f[perm]=(ans+n-1)/num_swap;
    }
  }

  return f[ff];
}

int main(void) {
  int ncas;
  assert(scanf("%d",&ncas)==1);
  while(ncas--) {
    int i,n;
    assert(scanf("%d",&n)==1);
    vi f(n);
    fi assert(scanf("%d",&f[i])==1);
    for (int use_monty=1;use_monty>=0;use_monty--) {
      df ans=fast(n,use_monty,f);
#ifdef TEST
      if (n <= 6) {
        // n is small, check the slow DP gets a similar answer.
        df ans2=slow(n,use_monty,f);
        if (fabs((ans2-ans)/ans)>1e-9) {
          printf("\nCase %d %d: %.9Lf %.9Lf!!\n",n,use_monty,ans,ans2);
          exit(1);
        }
      }

      // Check the MC algorithm gets a similar answer.
      df ans3=montecarlo(n,use_monty,f);
      if (fabs((ans3-ans)/ans)>0.02) {
        printf("\nCase %d %d: %.9Lf %.9Lf!\n",n,use_monty,ans,ans3);
        exit(1);
      }
#endif
      printf("%s %.6Lf",(use_monty?"Monty":" Carlos"), ans);
    }
    puts("");
  }

  return 0;
}

