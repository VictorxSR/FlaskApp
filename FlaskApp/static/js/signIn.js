$(function(){
	$('#btnSignIn').click(function(){
		
		$.ajax({
			url: '/signIn',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
                console.log(response);

                window.alert(response);

                if (response.startsWith("Welcome")){
                    window.location.href = "/";
                }
                else{
                    window.alert(response)
                }       
                
			},
			error: function(error){
				console.log(error);
            },
        });
        
       
	});
});