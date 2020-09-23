# Challenge 1 Results

## Input

File size: 1.9 GB

201,339,276 integers between 1 and 1,000,000,000 inclusive

### Test Cases

Submissions will be tested by searching the above input file for addends that
add to the following target values:

1. 480107308 (best case)
2. 193729123
3. 199029
4. 2500
5. 20
6. 25
7. 2000000000 (worst case)

## Results
| target value | greenjam98 O(n<sup>2</sup>) | hrshenk O(n) | thehinkydonut O(n<sup>2</sup>)| thunderhorse\* O(n) | veender O(n<sup>2</sup>)|
| --- | --- | --- | --- | --- | --- |
| 480107308 (best case) | 54.07s | 0.020s | 313.17s | 0.019s | 35.14s |
| 193729123 | 49.13s | 0.54s | 353.19s | 0.028s | 324.82s |
| 199029 | 44.67s | 2.65s | 455.81s | 0.48s | DNF |
| 2500 | 46.47s | 17.49s | 232.76s | 2.80s | DNF |
| 20 | 48.34s | 288.34s | 233. 55s | 27.46s | DNF |
| 25 | 44.86s | 227.31s | DNF | 27.86s | DNF |
| 2000000000 (worst case)| DNF | 229.22s | DNF | 199.41s | DNF |

\* Thunderhorse is judging this competition and therefore ineligible to
compete. His times are listed only for reference.

### Memory Utilization

#### gek

#### hrshenk
![Memory Utilization over Time](./memory_over_time/hrshenk.png)

#### thehinkydonut
![Memory Utilization over Time](./memory_over_time/thehinkydonut.png)

#### thunderhorse
![Memory Utilization over Time](./memory_over_time/thunderhorse.png)

#### veender
![Memory Utilization over Time](./memory_over_time/veender.png)
