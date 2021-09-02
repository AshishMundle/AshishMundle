// accept a character and check character is vowel or not 

#include<stdio.h>
int main ()
{
	char ch ;
	printf("enter any character :-");
	ch=getchar ();
	if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
	printf("entered character %c is vowel",ch);
	else
	printf("entered character %c is not vowel",ch);
	return 0;
}
