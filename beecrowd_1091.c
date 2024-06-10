#include <stdio.h>

int main()
{
    int casos;
    int div_x, div_y;
    int x, y;

    while (1)
    {
        scanf("%d", &casos);
        if (casos == 0)
        {
            break;
        }
        scanf("%d %d", &div_x, &div_y);
        for (int i = 0; i < casos; i++)
        {
            scanf("%d %d", &x, &y);
            if (x == div_x || y == div_y)
            {
                printf("divisa\n");
            }
            else if (x > div_x && y > div_y){
                printf("NE\n");
            }
            else if (x > div_x && y < div_y){
                printf("SE\n");
            }
            else if (x < div_x && y > div_y){
                printf("NO\n");
            }
            else if (x < div_x && y < div_y){
                printf("SO\n");
            }
        }
    }
}