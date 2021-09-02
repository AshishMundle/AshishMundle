// area of circle//

#include<stdio.h>
#include<conio.h>
#define PI 3.1452
main()
{
	float radius,area;
	printf("\n enter radius of circle:");
	scanf("%f",&radius);
	area=PI*radius*2;
	printf("\n area of circle is %.2f",area);
	getch();
}
