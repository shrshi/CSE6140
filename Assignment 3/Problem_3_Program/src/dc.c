#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"dc.h"


void dc(double *arr, int low, int high, double *sum, int *li, int *ri)
{
	//printf("in");
	int mid, leftlow, lefthigh, rightlow, righthigh,acrosslow, acrosshigh;
	double acrossum, leftsum, rightsum;
	if(low==high)
	{
		*sum = arr[low]; *li = low; *ri = high;
	}
	else
	{
		mid = (low+high)/2;
		dc(arr, low, mid, &leftsum, &leftlow, &lefthigh);
		dc(arr, mid+1, high, &rightsum, &rightlow, &righthigh);
		dc_helper(arr, low, high, mid, &acrossum, &acrosslow, &acrosshigh);
		if(leftsum>rightsum && leftsum>acrossum)
		{
			*sum = leftsum;
			*li = leftlow;
			*ri = lefthigh;
		}
		else if(rightsum>leftsum && rightsum>acrossum)
		{
			*sum = rightsum;
			*li = rightlow;
			*ri = righthigh;
		}
		else
		{
			*sum = acrossum;
			*li = acrosslow;
			*ri = acrosshigh;
		}
	}
}

void dc_helper(double *arr, int low, int high, int mid, double *acrossum, int *acrosslow, int *acrosshigh)
{
	double leftsum = -INFINITY, sum = 0.0, rightsum = -INFINITY;
	int i, maxleft, maxright;
	for(i=mid; i>=low;i--)
	{
		sum+=arr[i];	
		if(sum>leftsum)
		{
			leftsum=sum;
			maxleft=i;
		}
	}
	sum=0.0;
	for(i=mid+1;i<=high;i++)
	{
		sum+=arr[i];
		if(sum>rightsum)
		{
			rightsum=sum;
			maxright=i;
		}
	}
	*acrossum = leftsum+rightsum;
	*acrosslow = maxleft;
	*acrosshigh = maxright;
}

