// print sum of even number from 1 to 20 

#include<stdio.h>
int main()
{
	int num=20,i,sum;
	printf(" even number between 1 to 20 :");
	scanf("%d",&num);
	for (i=1;i<=num;i++)
	{
		if (i%2==0)
		{
			sum=sum+i;
		}
	}
	printf("sum of even number is %d",num);
	return (0);
}
