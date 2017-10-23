#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<dirent.h>
#include<unistd.h>
#include<sys/types.h>
#include<errno.h>
#include<sys/time.h>
#include<limits.h>
#include"dc.h"
#include"dp.h"

int main(int argc, char **argv)
{
	DIR *dir_p=NULL;
	struct dirent *dptr;
	FILE *data_file, *output_file_dc, *output_file_dp;
	char filename[50], t[20];
	char dest_dc[50], dest_dp[50];
	char *line, *token;
	int params[2], i, j;
	double *arr, max_sum;
	int max_li, max_ri;
	struct timeval start, end;
	
	dir_p = opendir("../data");	
	while((dptr=readdir(dir_p))!=NULL) //reading data files iteratively
	{
		if(strcmp(dptr->d_name, "..")==0 || strcmp(dptr->d_name, ".")==0 || strcmp(dptr->d_name, "10.txt")==0)
			continue;
		strcpy(dest_dc, "../output/sshivakumar9_output_dc_");
		strcpy(dest_dp, "../output/sshivakumar9_output_dp_");
		sprintf(filename, "../data/%s", dptr->d_name); 
		data_file = fopen(filename, "r");
		strcat(dest_dc, dptr->d_name);
		strcat(dest_dp, dptr->d_name);
		output_file_dc = fopen(dest_dc, "w");
		output_file_dp = fopen(dest_dp, "w");
		fgets(t, sizeof(t), data_file); t[strlen(t)-1]='\0';

		token = strtok(t, ","); i=0;
		while(token)
		{
			params[i] = atoi(token); //storing n and k in params
			token=strtok(NULL, ",");
			i++;
		}
		
		line = malloc(sizeof(char) * params[0] * 10);
		while(fgets(line, sizeof(char) * params[0] * 10, data_file))
		{
			line[strlen(line)-1]='\0';
			arr = (double*)malloc(sizeof(double)*params[0]);
			token = strtok(line, ","); i=0;
			while(token)
			{
				arr[i] = atof(token); // storing each problem instance in array
				token=strtok(NULL, ",");
				i++;
			}
			max_sum=0.0, max_li = -1, max_ri = -1;
			gettimeofday(&start, NULL);
			dc(arr, 0, params[0]-1, &max_sum, &max_li, &max_ri); // computing maximum contiguous subarray using divide and conquer
			gettimeofday(&end, NULL);
			fprintf(output_file_dc, "%.2f,%d,%d,%ld\n", max_sum, max_li+1, max_ri+1, (end.tv_sec * 1000000 + end.tv_usec) - (start.tv_sec * 1000000 + start.tv_usec));
			
			max_sum=INT_MIN, max_li=0, max_ri=0;
			gettimeofday(&start, NULL);
			dp(arr, params[0], &max_sum, &max_li, &max_ri); // computing maximum contiguous subarray using dynamic programming
			gettimeofday(&end, NULL);
			fprintf(output_file_dp, "%.2f,%d,%d,%ld\n", max_sum, max_li+1, max_ri+1, (end.tv_sec * 1000000 + end.tv_usec) - (start.tv_sec * 1000000 + start.tv_usec));

			free(line);
			free(arr);
			line=(char*)malloc(sizeof(char)*10*params[0]);
		}

	}
}

