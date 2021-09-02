// accept 3 paper marks less than 45 show "fail" or show "pass"

#include<stdio.h>
int main ()
{
	int p1,p2,p3;
	printf("enter 3 subject marks :-");
	scanf("%d%d%d",&p1,&p2,&p3);
	if(p1>45&&p2>45&&p3>45)
	printf("pass");
	else
	printf("fail");
	return 0;
}
