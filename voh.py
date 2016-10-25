import random


"""
=========
변수 결과
=========

=====  =====  =====
결과    
-------------------
count    A      B
=====  =====  ===== 
1       win     lose
2       lose    win
3       draw    draw
4       win     lose
5      lose    win
6      draw    draw
7      win     lose
8      lose    win
9      draw    draw
10     win     lose
=====  =====  =====


통계..
===============

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+


******************
1:가위 2:바위 3:보
******************
가위
    #. 바위에 진다.
    #. 보에 이긴다.

바위
    #. 보에 이긴다.
    #. 가위에 진다.
보 
    #. 가위에 진다.
    #. 바위에 이긴다.

.. image:: images.png
    :height: 200
    :width: 400
    :scale: 50
"""
def voh():
	"""
	 1:가위 2:바위 3:보
	"""
	count = 0
	while count<10:
		a = random.randrange(1,4)
		b = random.randrange(1,4)
		if a > b:
			# a is win.
			print("a:win  b:lose")
		elif a == b:
			# 
			print("draw    draw")
		elif a < b:
			# b is win. 
			print("b:win  a:lose")
		count+=1
voh()
