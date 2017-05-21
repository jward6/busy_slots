Populate a 7 day "week-view" showing availability in 1-hour time slices given an input
of availability start and stop time windows.

* Use the least number of 1-hour time slices

Input: Lists of dictionaries with a start and stop date time signaling the availability window.

[[{jn: xn, kn: yn}, {in+1: xn+1, kn+n: yn+1}], ]

Output: integer of total number of 1-hour time slices

Assumptions:
*  0 <= xn < yn <= 24
*  yn <= xn+1



