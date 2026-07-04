#include <iostream>

int main()
{

    int year;
    std::cin >> year;
    year += 1;

    while (1)
    {
        int a = year / 1000;
        int b = (year / 100) % 10;
        int c = (year / 10) % 10;
        int d = year % 10;

        if (a != b && a != c && a != d && b != c && b != d && c != d)
        {
            std::cout << year << std::endl;
            return 0;
        }

        year += 1;
    }
    return 0;
}