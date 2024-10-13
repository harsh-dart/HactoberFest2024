#include <vector>
#include <iostream>
using namespace std;
bool check(int k, int i, int j, vector<vector<char>> &b)
{
    char ch = k + '0';
    // row
    for (int c = 0; c < 9; c++)
    {
        if (b[i][c] == ch)
            return false;
    }
    // col
    for (int r = 0; r < 9; r++)
    {
        if (b[r][j] == ch)
            return false;
    }
    // box
    int r = (i / 3);
    int c = (j / 3);
    for (int rr = r * 3; rr < r * 3 + 3; rr++)
    {
        for (int cc = c * 3; cc < c * 3 + 3; cc++)
        {
            if (b[rr][cc] == ch)
                return false;
        }
    }
    return true;
}
bool solve(int i, int j, vector<vector<char>> &b)
{
    if (i == 9)
        return true;
    if (j == 9)
        return solve(i + 1, 0, b);

    if (b[i][j] != '.')
    {
        return solve(i, j + 1, b);
    }

    for (int k = 1; k <= 9; k++)
    {
        if (check(k, i, j, b))
        {
            b[i][j] = k + '0';
            if (solve(i, j + 1, b))
            {
                return true;
            }
            b[i][j] = '.';
        }
    }
    return false;
}

void solveSudoku(vector<vector<char>> &board) { solve(0, 0, board); }
int main()
{
    vector<vector<char>> board = {{'5', '3', '.', '.', '7', '.', '.', '.', '.'}, {'6', '.', '.', '1', '9', '5', '.', '.', '.'}, {'.', '9', '8', '.', '.', '.', '.', '6', '.'}, {'8', '.', '.', '.', '6', '.', '.', '.', '3'}, {'4', '.', '.', '8', '.', '3', '.', '.', '1'}, {'7', '.', '.', '.', '2', '.', '.', '.', '6'}, {'.', '6', '.', '.', '.', '.', '2', '8', '.'}, {'.', '.', '.', '4', '1', '9', '.', '.', '5'}, {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
    solveSudoku(board);
    for (auto &row : board)
    {
        for (auto &col : row)
            cout << col << " ";
        cout << endl;
    }
}
