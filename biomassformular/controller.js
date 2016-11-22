biogas = new Object();

$(document).ready(function() {
	$(".carbon").keyup(function () {
		var value = $(this).val();
		$(".pr_carbon").text(value);
		biogas.carbon = value;
		console.log(biogas)
	}).keyup();

	$(".hydrogen").keyup(function () {
		var value = $(this).val();
		$(".pr_hydrogen").text(value);
		biogas.hydrogen = value;
		console.log(biogas);
	}).keyup();

	$(".oxigen").keyup(function () {
		var value = $(this).val();
		$(".pr_oxygen").text(value);
		biogas.oxygen = value;
		console.log(biogas);
	}).keyup();

	$(".nitrogen").keyup(function () {
		var value = $(this).val();
		$(".pr_nitrogen").text(value);
		biogas.nitrogen = value;
		console.log(biogas);
	}).keyup();

	$(".in").keyup(function() {
		var result = biogas_formular(biogas.carbon, biogas.hydrogen, biogas.oxygen, biogas.nitrogen);
		$(".result").text(result);
	}).keyup();
})
