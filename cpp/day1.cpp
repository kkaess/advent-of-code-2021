#include <fstream>
#include <vector>
#include <iostream>
#include <omp.h>

using namespace std;

int main(int argc, const char *argv[])
{
    ifstream file;
    file.open("input/input_day1.txt");
    vector<int> vals{};
    char line[5];
    while (file.getline(line, 5).good())
    {
        vals.push_back(atoi(line));
    }
    file.close();
    int total = 0;
    #pragma omp parallel for shared(vals) reduction(+:total)
    for (size_t i = 1; i<vals.size(); i++)
    {
        if (vals[i] > vals[i-1])
        {
            total ++;
        }
    }

    cout << total << endl;

    total = 0;

   #pragma omp parallel for shared(vals) reduction(+:total)
    for (size_t i = 3; i<vals.size(); i++)
    {
        if (vals[i] > vals[i-3])
        {
            total ++;
        }
    }

    cout << total << endl;

    return 0;
}
