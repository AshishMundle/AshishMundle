// printing numbers in reverse order with difference of two

#include<stdio.h>
#include<math.h>
int main ()
{
	int i,j,x,n;
	int sum=1;
	printf("\n enter number of series and value ");
	scanf("%d%d",&n,&x);
	for(i=2;i<=n;i++)
	{
		sum=(float)pow(x,i)/i;
	}
	printf("\n sum=%d",sum);
	return 0;
}
