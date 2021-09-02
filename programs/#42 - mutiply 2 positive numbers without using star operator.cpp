// mutiply 2 positive numbers without using *operator 

#include<stdio.h>
int main ()
{
	int a,b,mul=0;
	printf("enter the two nos to multiply::");
	scanf("%d%d",&a,&b);
	for(int i=1;i<=b;i++)
	{
		mul=mul+a;
	}
	printf("multiplication of the nos is %d",mul);
}
