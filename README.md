Package for 06-643 project - Distillation column
===============

The Distillation Column Package is a package for analyzing and designing distillation columns. It provides functionalities for plotting McCabe-Thiele diagram, estimating the column dimensions, and calculating the column cost.

To make the package simpler, the relative volatality of the two components, bottoms composition mole fraction, along with the utility and capital cost constants are not inputted from the user.

## Package Functions

1) ***McCabe-Thiele plot***

**Function Name**: `mccabe_thiele`

**Description**:
This function plots McCabe-Thiele diagrams for a binary distillation process. Using matplotlib, we plot the equilibrium curve, stripping line, rectifying line, and the number of ideal stages required for separation.

2) ***Column Dimensions Calculation***

**Function Name**: `column_dimensions`

**Description**:
Estimates the dimensions of a distillation column, i.e the height and diameter.

3) ***Column Cost Estimation***
Function Name: `column_cost`

**Description**:
Estimates the cost for the distillation column (in USD)

***Parameters for all functions-***:

i) `feed_flow`: Feed flow rate (kg/hr)

ii) `xf`: Feed composition

ii) `xd`: Distillate composition
