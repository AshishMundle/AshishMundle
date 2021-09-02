// find the grade of a student when 4 subject marks are given 

#include<stdio.h>
main()
{
	float m1,m2,m3,m4,total,per;
	char grade ;
	printf("enter marks of subject:");
	scanf("%f%f%f%f",&m1,&m2,&m3,&m4);
	total=m1+m2+m3+m4;
	per=total/4;
		if(per>=85)
			grade='A';
		else if(per>=75&&per<85)
			grade='B';
		else if(per>=55&&per<75)
			grade='C';
		else if(per>=40&&per<55)
			grade='D';
		else
			grade='E';
	printf("percentage of %f,grade is %c,\n",per,grade);
	return 0;
}
