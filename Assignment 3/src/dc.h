
struct retval
{
	int low;
	int high;
	double val;
};

void dc(double *arr, int low, int high, double *sum, int *li, int *ri);
void dc_helper(double *arr, int low, int high, int mid, double *sum, int *li, int *ri);
