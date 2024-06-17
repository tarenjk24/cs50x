#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //accepting one command-line argument.

    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n ");
        return 1;
    }

    //opening file.
    FILE *file = fopen(argv[1], "r");
    //checking if it is valid.
    if (file == NULL)
    {
        printf("file invalid");
        return 2;
    }
    //initializing variables.
    int counter = 0;
    unsigned char buffer[512];
    FILE *recover = NULL;
    char *filea = malloc(8 * sizeof(char));
    //looping in file.
    while (fread(buffer, sizeof(char), 512, file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //writing file  name.
            sprintf(filea, "%03i.jpg", counter);
            recover = fopen(filea, "w");
            counter++;
        }
        if (recover != NULL)
        {
            fwrite(buffer, sizeof(char), 512, recover);
        }

    }
    free(filea);
    fclose(recover);
    fclose(file);

    return 0;

}