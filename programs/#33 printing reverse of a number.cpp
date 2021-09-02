// print reverse of a number 

#include<stdio.h>
int main ()
{
	int rev=0,no,rem;
	printf("enter number:");
	scanf("%d",&no);
	while(no>0)
	{ 
		rem=no%10;
		rev=rev*10+rem;
		no=no/10;
	}
	printf ("reverse no is:%d",rev);
	return 0;
}
