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
		t = 0;

		// If both elements are equal
		if(a[p1] == b[p2]) {
			c1 = 1, c2 = 1;
			// Count how many equal elements there are in list a
			while(a[p1] == a[p1+c1] && c1 < a.size()) {
				c1 += 1;
				cout << "igual\n";
				cout << a[p1] << " " << a[p1+c1] << "\n";
			}
			// Count how many equal elements there are in list b
			while(b[p2] == b[p2+c2] && c2 < b.size() ) {
				c2 += 1;
			}

			cout << c1 << " " << c2 << "\n";
			t = a[p1]*c1;
			t *= c2;
			s += t;
			p1 += c1;
			p2 += c2;
			cout << t << "\n";
		}
		else if(a[p1] < b[p2]) {
			p1 += 1;
		}
		else if(a[p1] > b[p2]) {
			p2 += 1;
		}
	}

	cout << s << "\n";

	return 0;
}
