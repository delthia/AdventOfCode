#include <bits/stdc++.h>

using namespace std;

int main() {
	string line;
	vector<int> a, b;
	int n1, n2;

	ifstream in("test-input");
	// ifstream in("input");
	while(getline(in, line)) {
		istringstream iss(line);
		iss >> n1 >> n2;

		a.push_back(n1);
		b.push_back(n2);
	}
	in.close();

	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	/*
	 * Part I
	 */
	cout << "Part I" << "\n";
	int t = a.size(), s = 0;	// Vector sizes
	for(int i = 0; i < t; i++) {
		s += abs(a[i]-b[i]);
	}

	cout << s << "\n";

	/*
	 * Part II
	 */
	cout << "Part II" << "\n";
	/*
	 * ci: Number of times that the current element is in the i vector
	 * pi: Curret position for the list i
	 * s: Similarity score
	 */
	int c1 = 1, c2 = 1, p1 = 0, p2 = 0;
	s = 0;
	while(p1 < a.size()) {
		while(a[p1+c1] == a[p1+c1-1]) {
			if(c1+1 >= a.size()) {
				break;
			}
			c1 += 1;
		}
		while(b[p2+c2] == b[p2+c2-1]) {
			if(c2+1 >= b.size()) {
				break;
			}
			c2 += 1;
		}
		s += a[p1]*b[p2];
		p1 += c1;
		p2 += c2;
		cout << s << "\n";
	}

	cout << s << "\n";

	return 0;
}
