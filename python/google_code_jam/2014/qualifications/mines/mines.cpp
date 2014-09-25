// Author: Sahand Saba <sahands@gmail.com>
#include <unistd.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define valid(x, y) (x > 0 && x <= R && y >0 && y <= C)
#define xstart max(x - 1, 1)
#define ystart max(y - 1, 1)
#define xend min(R, x + 1)
#define yend min(C, y + 1)

// Since C <= 50, a 64 bit number should be enough to keep track of it
typedef unsigned long long row;
const int N = 52;  // R <= 50 plus "padding" on two sides!
row lucky[N];
row revealed[N];
int R, C, M;

void print_state() {
    cout << "-- lucky --" << endl;
    for(int x = 1; x <= R; x++ ){
        for(int y = 1; y <= C; y ++) {
            cout << (1 & (lucky[x] >> y));
        }
        cout << endl;
    }
    cout << "-- revealed --" << endl;
    for(int x = 1; x <= R; x++ ){
        for(int y = 1; y <= C; y ++) {
            cout << (1 & (revealed[x] >> y));
        }
        cout << endl;
    }
}

void print_solution(int sx, int sy) {
    int m = 0;
    for(int x = 1; x <= R; x++ ){
        for(int y = 1; y <= C; y ++) {
            if(x == sx && y == sy) {
                cout << 'c';
                continue;
            }
            if(1 & (revealed[x] >> y)) {
                cout << '.';
            } else {
                m ++;
                cout << '*';
            }
        }
        cout << endl;
    }
    if(m != M) {
        cout << "WARNING: m != M" << endl;
    }
}

bool is_revealed(int x, int y) {
    return revealed[x] & (1 << y);
}

int update_revealed(int x, int y) {
    int c = 0;
    for(int xx = xend; xx >= xstart; xx--) {
        for(int yy = yend; yy >= ystart; yy--) {
            row mask = 7 << (yy - 1);
            if((lucky[xx - 1] & mask) |
               (lucky[xx]     & mask) |
               (lucky[xx + 1] & mask)) {
                c ++;
                revealed[xx] |= 1 << (yy);
            } else {
                revealed[xx] &= ~(1 << (yy));
            }
        }
    }
    return c;
}

int count_revealed_neighbours(int x, int y) {
    int c = 0;
    for(int xx = xend; xx >= xstart; xx--) {
        for(int yy = yend; yy >= ystart; yy--) {
            if(is_revealed(xx, yy)) {
                c++;
            }
        }
    }
    return c;
}

void set_lucky(int x, int y, bool val) {
    if(val) {
        lucky[x] |= 1 << y;
    } else {
        lucky[x] &= ~(1 << y);
    }
}

bool get_lucky(int x, int y) {
    return lucky[x] & (1 << y);
}


// Let's see if efficient backtracking can solve this one!
// Call a tile with no mines in its neighbouring tiles a "lucky" tile.
// Lucky tiles will reveal their neighbours.
// This function will make the tile at (x, y) lucky if possible, and then
// try to win recursively.
bool backtrack(int x, int y, int S) {
    if(S < 0) {
        return false;  // Too few mines
    }

    if(S == 0) {
        return true;  // We won!
    }

    int revealed = count_revealed_neighbours(x, y);
    set_lucky(x, y, true);
    int diff = update_revealed(x, y) - revealed;
    if(S - diff == 0) {
        return true;  // We won!
    }

    // print_state();
    // cout << "Diff = " << diff << endl;
    // usleep(1000 * 1000);

    for(int xx = xend; xx >= xstart; xx--) {
        for(int yy = yend; yy >= ystart; yy--) {
            if(xx == x && yy == y) continue;
            if(!get_lucky(xx, yy)) {
                if(backtrack(xx, yy, S - diff)) {
                    return true;
                }
            }
        }
    }

    // Clean up
    set_lucky(x, y, false);
    update_revealed(x, y);

    return false;
}


void init() {
    for(int i = 0; i <= R + 1; i++) {
        lucky[i] = 0;
        revealed[i] = 0;
    }
}

bool solve(int x, int y) {
    init();

    int S = R * C - M;
    if(S == 1) {
        set_lucky(0, 0, true);
        return true;
    }
    if((R==2 || C == 2) && (M % 2 == 1)) {
        return false;
    }

    return backtrack(x, y, S);
}


int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> R >> C >> M;
        cout << "Case #" << t << ":" << endl;
        // cout << R << " "  << C << " "  << M << " " << endl;
        bool possible = false;
        int x = 1, y = 1;
        // for(int x = 1; !possible && x <= R; x++) {
        //     for(int y = 1; !possible && y <= C; y++) {
                possible = solve(x, y);
                if(possible) {
                    // cout << "Possible" << endl;
                    print_solution(x, y);
                }
        //     }
        // }
        if(!possible) {
            cout << "Impossible" << endl;
            // cout << R << " "  << C << " "  << M << " " << endl;
        }
        cerr << t << endl;
    }

    return 0;
}
