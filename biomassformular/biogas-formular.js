function biogas_formular (a, b, c, d) {
	// a is mol of Carbon
	// b is mol of Hydrogen
	// c is mol of Oxigen
	// d is mol of Nitrogen
	var ch4 = ((4 * a) + b - (2 * c) - (3 * d))/8;
	var co2 = ((4 * a) - b + (2 * c) + (3 * d))/8;
	var nh3 = d;
	var h2o = ((4 * a) - b - (2 * c) + (3 * d))/4;
	var result = "it returns " + ch4 + " of CH4, " + co2 + " of CO2 and " + nh3 + " of NH3" + " and need " + h2o + " of H2O for chemical reaction to make Biogas";
	return result;
}
