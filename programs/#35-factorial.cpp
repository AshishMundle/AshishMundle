// factorial 

#include<stdio.h>
int main()
{
	int n,fact=1;
	printf("enter any number:");
	scanf("%d",&n);
	while(n>0)
	{
		fact*=n;
		--n;
	}
	printf("factorial=%d",fact);
	return 0;
}
