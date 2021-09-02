// checking the number odd or even 

#include <stdio.h>
int main ()
{
	int n;
	printf("enter any number \n");
	scanf("%d",&n);
	if (n%2==0)
	{
		printf("\n %d is even ",n);
	}
	else 
	{
		printf("\n %d is odd",n);
	}
	return 0;
}
