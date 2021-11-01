$(function(){
	$('.submit-button').click(function(){
		const test1 = $('#test1').val();
		const test2 = $('#test2').val();
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
});