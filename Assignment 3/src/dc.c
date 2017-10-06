#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"dc.h"


struct retval dc(double *arr, int low, int high)
{
	struct retval r, rl, ra, rr;
	int mid;
	if(low==high)
	{
		r.low=low; r.high=high; r.val=arr[low];
		return r;
	}
	else
	{
		mid = (low+high)/2;
		rl = dc(arr, low, mid);
		rr = dc(arr, mid+1, high);
		ra = dc_helper(arr, low, high, mid);
		printf("%d, %d", low, high);
		if(rl.val>rr.val && rl.val>ra.val)
			return rl;
		else if(rr.val>rl.val && rr.val>ra.val)
			return rr;
		else
			return ra;
	}
}

struct retval dc_helper(double *arr, int low, int high, int mid)
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
	struct retval r;
	r.low=maxleft; r.high=maxright; r.val=leftsum+rightsum;
	return r;
}




