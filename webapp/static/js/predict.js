$(document).ready(function(){
	$('.submit-button').click(function(){
		const stm_km_tot_mld = $('#stm_km_tot_mld').val();
		const stm_km_van_mld = $('#stm_km_van_mld').val();
		const smt_reactie_duur = $('#smt_reactie_duur').val();
		const meldtijd = $('#meldtijd').val();
		const stm_techn_mld = $('stm_techn_mld').val();
		const stm_prioriteit = $('stm_prioriteit').val();
		const Oorzaak = $('Oorzaak').val();
		const stm_equipm_soort_mld = $('stm_equipm_soort_mld').val();
		const traject = $('traject').val();
		const stm_contractgeb_gst = $('stm_contractgeb_gst').val();
		$.ajax({
			url: '/',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
		$('.result').addClass('active');
	});
	$('.js-example-basic-single').select2();
});