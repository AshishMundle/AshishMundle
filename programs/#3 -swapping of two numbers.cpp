/* swapping of two numbers*/

#include<stdio.h>
int main ()
{
	int a=18,b=8;
	printf(" before swap a=%d ,b=%d ",a,b);
	
	a=a+b; //a=26(18+8)
	b=a-b; //b=10(18-8)
	a=a-b; //a=16(26-10)
	printf("after swap a=%d,b=%d",a,b);
	return 0;
}
