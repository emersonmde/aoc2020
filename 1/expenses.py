#!/usr/bin/env python3

from itertools import combinations

entries = [
    1825,
    1944,
    1802,
    1676,
    1921,
    1652,
    1710,
    1952,
    1932,
    1934,
    1823,
    1732,
    1795,
    1681,
    1706,
    1697,
    1919,
    1695,
    2007,
    1889,
    1942,
    961,
    1868,
    1878,
    1723,
    416,
    1875,
    1831,
    1890,
    1654,
    1956,
    1827,
    973,
    1947,
    1688,
    1680,
    1808,
    1998,
    1794,
    1552,
    1935,
    1693,
    1824,
    1711,
    1766,
    1668,
    1968,
    1884,
    217,
    2003,
    1869,
    1658,
    1953,
    1829,
    1984,
    2005,
    1973,
    428,
    1957,
    1925,
    1719,
    1797,
    321,
    1804,
    1971,
    922,
    1976,
    1863,
    2008,
    1806,
    1833,
    1809,
    1707,
    1954,
    1811,
    1815,
    1915,
    1799,
    1917,
    1664,
    1937,
    1775,
    1685,
    1756,
    1940,
    1660,
    1859,
    1916,
    1989,
    1763,
    1994,
    1716,
    1689,
    1866,
    1708,
    1670,
    1982,
    1870,
    1847,
    1627,
    1819,
    1786,
    1828,
    1640,
    1699,
    1722,
    1737,
    1882,
    1666,
    1871,
    1703,
    1770,
    1623,
    1837,
    1636,
    1655,
    1930,
    1739,
    1810,
    1805,
    1861,
    1922,
    1993,
    1896,
    1760,
    2002,
    1779,
    1633,
    1972,
    1856,
    1641,
    1718,
    2004,
    1730,
    1826,
    1923,
    1753,
    1735,
    660,
    1988,
    1796,
    1990,
    1720,
    1626,
    1788,
    1700,
    942,
    1902,
    1943,
    1758,
    1839,
    1924,
    938,
    1634,
    1724,
    1983,
    1683,
    1687,
    1904,
    1907,
    1757,
    2001,
    1910,
    1849,
    1781,
    1981,
    1743,
    1851,
    2009,
    619,
    1898,
    1891,
    1751,
    1765,
    1959,
    1888,
    1894,
    1759,
    389,
    1964,
    1900,
    1742,
    1672,
    1969,
    1978,
    1933,
    1906,
    1807,
    1867,
    1838,
    1960,
    1814,
    1950,
    1918,
    1726,
    1986,
    1746,
    2006,
    1949,
    1784
]

checked = {}

# O(n^2)
def part1():
    for a in entries:
        for b in entries:
            if a + b == 2020:
                return a * b;

# O(n^2)
def part1v2():
    results = set()
    for entry in entries:
        results.add(entry)
        result = 2020 - entry
        if result in results:
            return result * entry

# O(n choose 2)
def part1v3():
    for a, b in list(combinations(entries, 2)):
        if a + b == 2020:
            return a * b
                
# O(n^3)
def part2():
    for a in entries:
        for b in entries:
            for c in entries:
                if a + b + c == 2020:
                    return a * b * c;

# O(n^2)
def part2v2():
    results = set()
    for first_entry in entries:
        for second_entry in entries:
            results.add(first_entry)
            results.add(second_entry)
            result = 2020 - first_entry - second_entry
            if result in results:
                return result * first_entry * second_entry

# O(n choose 3)
def part2v3():
    for a, b, c in list(combinations(entries, 3)):
        if a + b + c == 2020:
            return a * b * c


if __name__ == "__main__":
    #print(part1())
    #print(part2())
    print(part1())
    print(part1v2())
    print(part1v3())
    print(part2())
    print(part2v2())
    print(part2v3())
    
