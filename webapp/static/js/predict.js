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

				$('body').removeClass('no-scroll');

				$('html, body').animate({
					scrollTop: $("#result").offset().top - 400
				}, 1000);

				$("canvas#probChart").remove();
				$("div.prob-container").append('<canvas id="probChart" width="400" height="400"></canvas>');

				data = response.graphdata[2];

				var ctx = $('#probChart');

				const prob_chart = new Chart(ctx, {
					type: 'doughnut',
					data: {
						labels: response.graphdata[0],
						datasets: [{
							label: 'Zekerheid bij de voorspellen',
							data: response.graphdata[1],
							backgroundColor: response.graphdata[2]
						}]
					},
					options: {
						plugins: {
						  datalabels: {
							  display: true
						  }
						}
					  }
				});

				$('#hersteltijd').text(response.hersteltijd)
				$('#speling').text(response.speling)
				$('#result').addClass('active');
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
		$('#result').removeClass('active');
		// $('.submit-button').prop('disabled', false);

		$('html, body').animate({
			scrollTop: $("section").offset().top - 200
		}, 400);

		setTimeout(function() {
			$('body').addClass('no-scroll');
		}, 400);

		// ENABLE TO RESET INPUTS ON RELOAD
		// $('form')[0].reset();
	})
});