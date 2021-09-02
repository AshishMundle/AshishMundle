// print fibonacci series 

#include<stdio.h>
int main()
{
	int i,n,x=0,y=1,z;
	printf("\n enter the range :");
	scanf("%d",&n);
	printf("%4d%4d",x,y);
	for(i=1;i<=n;i++);
	{
		z=x+y;
		printf("%4d",x);
		x=y;
		y=z;
	}
	return 0;
}
