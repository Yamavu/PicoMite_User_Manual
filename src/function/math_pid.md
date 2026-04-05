### MATH(PID channel, setpoint!, measurement))

This function must be called in the PID callback subroutine for the `channel`
specified and returns the output of the controller function.

The `setpoint` value is the desired state that the controller is trying to achieve.

The `measurement` is the current value of the real world.

https://www.thebackshed.com/forum/ViewTopic.php?FID=16&TID=17263
For an example of setting up and running a PID controller