$(document).ready(function() {

	$('form').on('submit', function(event) {
        alert('제출 완료')
		$.ajax({
			data : {
				name : $('#nameInput').val(),
				email : $('#emailInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});