#include <iostream>
#include <algorithm>

using namespace std;

int main()
{

    int test_cases;
    int result;

    std::cin >> test_cases;

    for (int i = 0; i < test_cases; i++)
    {

        int grid[2][2] = {0};

        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 2; k++)
            {

                std::cin >> grid[j][k];
            }
        }

        int temp1 = std::max({grid[0][0], grid[0][1], grid[1][0]}) + grid[1][1];
        int temp2 = std::max({grid[1][0], grid[0][0], grid[1][1]}) + grid[0][1];
        int temp3 = std::max({grid[1][1], grid[0][1], grid[1][0]}) + grid[0][0];
        int temp4 = std::max({grid[0][1], grid[0][0], grid[1][1]}) + grid[1][0];

        std::cout << min({temp1, temp2, temp3, temp4}) << endl;
    }

    return 0;
}
