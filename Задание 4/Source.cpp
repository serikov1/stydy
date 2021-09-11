#include<iostream>
int main() {
	int n, x, t;
	t = 0;
	std::cin >> n;
	for (int i = 0; i < n; i++) {
		std:: cin >> x;
		if (abs(x) > abs(t))
			t = x;
	}
	std::cout << t;
	return 0;
}