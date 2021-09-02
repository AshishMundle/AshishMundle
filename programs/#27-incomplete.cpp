// accept a character and check character is upper case , lower case ,digit or special symbol

#include <stdio.h>
int main
{
	float ch;
	char ch ;
	printf("\n enter any character:");
	scanf("%c",&ch);
	if(ch>=65&&ch<=90)
	printf("\n % is uper case",ch);
	else if (ch>=97&&ch<=122)
	printf("\n %c is lower case",ch);
	else if (ch>=48&&ch<=57)
	printf("\n %c is digit",ch);
	else 
	printf("\n %c is special symbol",ch);
	return 0;
}
