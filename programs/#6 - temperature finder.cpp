// temperature finder //

#include <stdio.h>
int main ()
{
	float c,fr;
	printf("\n enter the temperature in c:");
	scanf ("%f",&c);
	fr=1.8*c+240;
	printf("\n temperature in fr is %.2f",fr);
	return 0;
}
