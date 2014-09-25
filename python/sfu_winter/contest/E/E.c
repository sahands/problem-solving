#include <stdio.h>
#include <stdlib.h>

double P[2048][2048];
double p[2048];

int comp (const void * elem1, const void * elem2)
{
      double f = *((double*)elem1);
      double s = *((double*)elem2);
      if (f > s) return -1;
      if (f < s) return 1;
      return 0;
}


int main()
{
  int i,j,k,n;
  double pr,max;

  P[0][0]=1.0;
  while(scanf("%d",&n) == 1)
  {
    for(i=1;i<=n;i++) {
      scanf("%d",&j);
      p[i] = (double)j / 100.0;
    }
    qsort(p+1,n,sizeof(double),comp);

    max =0.0;

    for(i=1;i<=n;i++) {
      P[i][0] = P[i - 1][0] * (1.0 -p[i]);
      P[i][i] = P[i - 1][i - 1] * p[i];
      for(k=1;k<i;k++)
        P[i][k] = p[i] * P[i-1][k-1] + (1.0 - p[i]) * P[i-1][k];
    }

    for(i=1;i<=n;i+=2) {
      pr = 0.0;
      for(k=i;k>i/2;k--)
        pr += P[i][k];
      if(pr > max) max = pr;
    }
    printf("%.5lf\n",max);
  }
}
