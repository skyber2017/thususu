$(document).ready(function() {
	$("#login").click(function() {
		$(this).html('<img src="/static/login/img/loading.gif" style="width:25px;height:auto;">');
		email = $("email").val();
		pass = $("password").val();
		if(email == "" || pass == ""){
			alert("Không được bỏ trống");
		}
		$.ajax({
			url: '/login',
			type: 'POST',
			data: $("form").serialize(),
		})
		.done(function(data) {
			$('#login').html("Đăng nhập");
			$('#result').removeClass('hidden');
			$('#result').html(data.mess);
			if(data.result){
				window.location.href = '/';
			}
			//console.log(data);
		})
		.fail(function() {
			$('#login').html("Đăng nhập");
			$('#result').html("Đã có lỗi xảy ra. Vui lòng liên hệ Admin.")
		})

	});
});