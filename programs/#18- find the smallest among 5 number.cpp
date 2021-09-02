// find the smallest among 5 number 

#include<stdio.h>
int main ()
{
	int n1,n2,n3,n4,n5,min;
	printf("\n enter five numbers :- ");
	scanf("%d%d%d%d%d",&n1,&n2,&n3,&n4,&n5);
	min=n1;
	if(min>n2)
		min=n2;
	if(min>n3)
		min=n3;
	if(min>n4)
		min=n4;
	if(min>n5)
		min=n5;
	printf("\n smallest element is %d",min);
	return 0;
}
