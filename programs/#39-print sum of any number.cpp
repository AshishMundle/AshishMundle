// print sum of any number 

#include<stdio.h>
int main ()
{
	int i,n,sum=0;
	printf("\n enter the number :");
	scanf("%d",&n);
	for(i=0;i<=n;++i)
	{
		sum=sum+i;
	}
	printf("\n sum of number is %d",sum);
	return 0;
}
