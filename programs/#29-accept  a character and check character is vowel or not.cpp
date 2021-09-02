// accept  a character and check character is vowel or not

#include<stdio.h>
#include<process.h>
int main()
{
	char ch;
	printf("\n enter any character:");
	ch=getchar ();
	switch (ch)
	{
		case'a':
		case'e':
		case'i':
		case'o':
		case'u':
		printf("\n %c is vowel",ch);
		break;
		default:printf("\n %c is constant",ch);
		break;
	}
	return 0;
}
