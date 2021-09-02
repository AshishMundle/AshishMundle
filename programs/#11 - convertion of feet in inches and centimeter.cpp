// convertion of feet in inches & centimeter

#include <stdio.h>
int main ()
{
	float feet,inches,cm;
	printf("\n enter height in feet = ");
	scanf("%f",&feet);
	inches=12*feet;
	cm=feet*30.48;
	printf("\n your result =%.2f inches and %.2f cm",inches,cm);
	return 0;
}
