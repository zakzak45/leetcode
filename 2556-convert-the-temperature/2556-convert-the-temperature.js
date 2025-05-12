/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function(celsius) {
     farenheight =(celsius*9/5)+32
     kelvin = celsius + 273.15

  return [kelvin ,farenheight]


};