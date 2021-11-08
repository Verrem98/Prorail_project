	$(document).ready(function(){
	$('.submit-button').click(function(){
		const stm_km_tot_mld = $('#stm_km_tot_mld').val();
		const stm_km_van_mld = $('#stm_km_van_mld').val();
		const stm_reactie_duur = $('#stm_reactie_duur').val();
		const meldtijd = $('#meldtijd').val();
		const stm_techn_mld = $('#stm_techn_mld').val();
		const stm_prioriteit = $('#stm_prioriteit').val();
		const Oorzaak = $('#Oorzaak').val();
		const stm_equipm_soort_mld = $('#stm_equipm_soort_mld').val();
		const traject = $('#traject').val();
		const stm_contractgeb_gst = $('#stm_contractgeb_gst').val();
		const stm_fh_status = $('#stm_fh_status').val();
		$.ajax({
			url: '/' + $(this).attr('data-url'),
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#hersteltijd').text(response.hersteltijd)
				$('#speling').text(response.speling)
				$('.result').addClass('active');
				$('#prob_chart').attr('src', "static/images/decision_tree_pred_prob.png")
				$(this).prop('disabled', true);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
	$('.js-example-basic-single').select2({ width: '300px' });

	$('#reset').click(function (){
		$('.result').removeClass('active');
		$('.submit-button').prop('disabled', false);
		$('form')[0].reset();
	})
});