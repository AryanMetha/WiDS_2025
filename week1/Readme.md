My results with polices implemented are :

    Policy: random_policy     | Avg Return:   -2.932 | Avg Steps:  28.46
    Policy: monotonous_policy | Avg Return:    9.306 | Avg Steps:   6.64
    Policy: wildcard_policy   | Avg Return:  -49.976 | Avg Steps:  48.20

    1.Random policy:
        -chooses left or right at random with equal probability.
        -no use of info from the state or history.
    2.Monotonous policy:
        -moves in only one direction until it hits boundary, then it reverses its direction.
    3.Wildcard Policy:
        -prefer moving toward the center where each time the center changes.
        -if the state is left of center, move right and change center to center of left half.
        -if the state is right of center, move left and change center to center of right half.
        -"The modified wildcard policy performs better than a static center-based policy, as it avoids getting stuck at a single location by dynamically adjusting its center".

******************************************************
OBSERVATIONS ARE :
    -Monotonous policy received highest average return and this may be due to small size of 1D grid and ordered but not random stepping policy.
    -Random policy is moderately poor as it remains unguided.
    -Wildcard Policy with my modifications performs bad may be because of oscillations near center reaching step limit and getting large penalty.

*****************************************************
How would your apprach towards designing the wildcard policy change if the agent was allowed to loop around???
    That is to say , taking a right step on the righ most cell will transport you to the left most cell.There would be no boundaries changing its nature from linear to circular.Then there would be no meaningful center.Then it may have two paths to goal and makes it reward driven rather than state driven for choosing a path.

*****************************************************
CONCLUSION:
    Policy making makes a key role in performance...