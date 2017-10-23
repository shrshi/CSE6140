#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"dp.h"


void dp(double *arr, int n, double *max_sum, int *max_li, int *max_ri)
{
	double max_here=0.;
	int i, s=0;

	for(i=0; i<n; i++)
    {
        max_here += arr[i];
 
        if (*max_sum < max_here)
        {
            *max_sum = max_here;
            *max_li = s;
            *max_ri = i;
        }
 
        if (max_here < 0)
        {
            max_here = 0;
            s = i+1;
        }
    }
}