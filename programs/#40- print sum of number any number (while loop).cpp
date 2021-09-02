#include<stdio.h>
#include<conio.h>
main()
{
int num,rem,sum=0;
printf("\n Enter any numbers : ");
scanf("%d",&num);
while(num>0)
{
  rem=num%10;
  sum+=rem;
  num/=10;

}
printf("\nSum = %d ",sum);
getch();
}
