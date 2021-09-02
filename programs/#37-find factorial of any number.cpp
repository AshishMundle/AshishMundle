// find factorial of any number 

#include<stdio.h>
int main()
{
	int num,fact=1;
	printf("enter any number:");
	scanf("%d",num);
	for (i=1;i<=20;++i)
	{
		fact=fact*i;
    }
	printf("fact=%d",fact);
	return 0;
}
