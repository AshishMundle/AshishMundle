/* simple calculator */

#include<stdio.h>
int main ()
{
	int a,b,res ;
	printf (" enter any two numbers :-");
	scanf("%d",&a);
	scanf("%D",&b);
	res=a+b;
	printf("\n addition of number is %d",res);
	res=a*b;
	printf("\n multiplication of number is %d",res);
	res=a-b;
	printf("\n substraction of number is %d",res);
	res=a/b;
	printf("\n division of number is %d",res);
	return 0;
	
}
