#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    //getting text.
    string text = get_string("text: ");
    //initialization( words = 1 there is always one more word for number of spaces).
   int w = 1;
   int l=0;
   int s=0;


      //counting numbers of words letters and sentences.
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            l++;
        }
        else if (text[i] == ' ')
        {
            w++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?' )
        {
            s++;
        }
    }
    //calculating average then index.
    float sentence = s / (float)w * 100;
    float letters = l / (float)w * 100;
    int index = round(0.0588 * letters - 0.296 * sentence - 15.8);
    //camparing to display the grade of the text.
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 10)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}