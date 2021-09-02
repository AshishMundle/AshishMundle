// adding substracting multiplying dividing using switch case

#include<process.h>
#include<stdio.h>
int main()
{
	int ch,a,b,res;
	printf("\n enter two number:- ");
	scanf("%d%d",&a,&b);
	printf("\n1.add\n2.mul\n3.sub\n4.div\n5.exit");
	printf("\n enter any choice:-");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1:
			printf("\n result=%d",a+b);
			break;
		case 2:
			printf("\n result=%d",a*b);
			break;
		case 3:
			printf("\n result=%d",a-b);
			break;
		case 4:
			printf("\n result=%d",a/b);
			break;
		case 5:
			exit (0);
		default:
			printf("\n wrong selection");
	}
	return 0;
}
