#include <stdio.h>
#include <string.h>

int swap(int x, int y);
int numbers[] = {6,2,4,7,1,3,8,5,9};

int main(void)
{
    int counter = 1;
    size_t n = sizeof(numbers)/sizeof(int);

    while ( n > 0 || counter > 0)
    {
        for (int i = 0; i < (n-1); i++)
        {
            if (numbers[i] > numbers[i+1])
            {
                numbers[i], numbers[i+1] = swap(numbers[i], numbers[i+1]); // Returning and swaping both values from the swap function
                counter += 1;
            }
        }
        counter = 0;
        n -= 1;
    }
    for (int j = 0; j < 9; j++)
    {
        if (j == 8)
        {
            printf("%i.\n", numbers[j]);
        }
        else
        {
            printf("%i, ", numbers[j]);
        }
    }
}

int swap(int x, int y)
{
    int temp = x;
    x = y;
    y = temp;
    return x, y;
}
