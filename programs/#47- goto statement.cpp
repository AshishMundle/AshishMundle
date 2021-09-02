// goto statement 

#include<stdio.h>
main()
{
	int a,b,c;
	printf( "\n enter value of a & b:- ");
	scanf("%d%d",&a,&b);
	if(b==0)
		goto error;
		c=a/b;
		printf("\n answer=%d",c);
	if(b==0)
		error:printf("\n try to divie by zero number");
		return 0;
}
