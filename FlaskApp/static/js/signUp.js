$(function(){
	$('#btnSignUp').click(function(){
		
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				

				if(response == "Usuari donat d'alta"){
					window.alert(response);
					window.location.href = "/showSignIn";
				}
				else{
					window.alert(response);
				}
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
