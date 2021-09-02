// finding sum of first and last digit of 5 digit number//

#include <stdio.h>
int main()
{
	int a,b,sum,num;
	printf("/n enter any 5 digit number");
	scanf("%d",&num);
	a=num%10;
	b=num/10000;
	sum=(a+b);
	printf("/n the sum is: %d ",sum);
	return 0;	
}
