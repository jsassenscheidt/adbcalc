# adbcalc - Amsterdam UMC Database calculator

## Description 

The aim of this project is to create a calculator for the [Amsterdam
UMC Critical Care Database](https://github.com/AmsterdamUMC/AmsterdamUMCdb). When observing a time period, one can not calculate the exact dose of an infused fluid or drug if the start or the stop timestamp lies outside the observation period. To overcome this problem, adbcalc takes the start and stop time of a medication infusion, the dose per time unit and the end of the observation period. With these information, adbcalc calculates the given dose from start to stop or from start to the end of the observation period, respectively. 