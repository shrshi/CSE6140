
struct retval
{
	int low;
	int high;
	double val;
};

struct retval dc(double *arr, int low, int high);
struct retval dc_helper(double *arr, int low, int high, int mid);
