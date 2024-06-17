#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //intialization.
    int x;

   do
   {
        //getting pyramid height.

        x = get_int("Enter pyramid height between 1-8: ");

   }
      //testing if it is between 1 to 8.

   while(x < 1 || x >8);

    //building pyramid.
          for (int j = 0; j < x; j++)
        {
            for(int i=0; i < x; i++)

              {
                if (j + i  < x - 1)
                //display dots.
                printf(" ");
                else
                //display #.
                printf("#");
              }
             //going back to line.
             printf("\n");
        }
    }



