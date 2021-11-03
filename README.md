# Installation

```
$ pip install opencv-contrib-python
```

# Tutorial followed
https://youtu.be/oXlwWbU8l2o

# Rotation :

Suppose we have a point **P(x,y)** at an angle **alpha** and distance **r** from the origin as shown below. Now we rotate the point **P** about the origin by an angle **theta** in the clockwise direction. The rotated coordinates can be obtained as shown below.

<center><img src="https://i2.wp.com/theailearner.com/wp-content/uploads/2020/11/rotation.jpg?resize=768%2C834&ssl=1" /></center>

<br>

So, we just need to create the transformation matrix **(M)** and then we can rotate any point as shown above. That’s the basic idea behind rotation. Now, let’s take the case with an adjustable center of rotation **O(x0, y0)**.

<center><img src="https://i0.wp.com/theailearner.com/wp-content/uploads/2020/11/rotation1-2.jpg?resize=768%2C772&ssl=1" /></center>

**Note:** The above expression is for clockwise rotation. For anti-clockwise minor changes in the sign will occur.