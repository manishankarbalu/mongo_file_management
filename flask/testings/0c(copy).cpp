#include<iostream>
using namespace std;
int maxOnesIndex(int arr[], int n)
{
    for(int i=0;i<n;i++)
            arr[i]=-arr[i];
int lc=0;int rc=0;

for(int i=0;i<n;i++)
     {
           if(arr[i]==-1)
                       lc++;
            else
             {
               arr[i]=lc;
               lc=0;
             }

     }
for(int i=n-1;i>=0;i--)
     {
           if(arr[i]==-1)
                       rc++;
            else
             {
               arr[i]+=rc;
               rc=0;
             }

     }

int maxindex=0;lc=arr[0];
for(int i=1;i<n;i++)
      if(lc<arr[i])maxindex=i;

for(int i=0;i<n;i++)
            cout<<arr[i];
return maxindex;
}
int main()
{
    int arr[] = {1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "Index of 0 to be replaced is "
         << maxOnesIndex(arr, n);


    return 0;
}
