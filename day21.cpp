#include <stdio.h>
#include <set>
// part 2 
std::set<int>  eSet;
int test()
{
	int a = 0, b = 0, c = 0, d = 0;
	int e = 123;
line1: e &= 456;
	if (e == 72)
	{
		e = 0;
		line6: d = e | 0x10000;
		e = 15466939;
		while (1)
		{
			c = d & 0xFF;
			e += c;
			e &= 0xFFFFFF;
			e *= 65899;
			e &= 0xFFFFFF;
			if (256 > d)
			{
				if (eSet.find(e) == eSet.end())
				{
					eSet.insert(e);
					printf("maxE: %d\n", e);
				}
				else
					return;
				if (e == a)
					break;
				else
					goto line6;
			}
			else
			{
				d = int(d / 256);
			}
		}

	}
	else
		goto line1;
}

#include <limits>
int main()
{
	test();
	return 0;
}
