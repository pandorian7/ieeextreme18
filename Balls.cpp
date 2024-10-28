#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long N, hits;
    hits = 0;
    int K;
    cin >> N >> K;
    vector<int> E(K);
    for (int i=0; i<K; i++) {
        cin >> E[i];
    }
    vector<char> m(N, 0);
    for (auto val : E) {
        for (long long i=val; i<N; i+=val) {
            if (!m[i]){
                hits++;
            }
            m[i] = 1;
        }
    }
    cout << hits;
}