$(document).ready(function() {
	$("#login").click(function() {
		$(this).html('<img src="/static/login/img/loading.gif" style="width:25px;height:auto;">');
		$.ajax({
			url: '/login',
			type: 'POST',
			data: $("form").serialize(),
		})
		.done(function(data) {
			$('#login').html("Đăng nhập");
			if(data != "True"){
				console.log(data);
			}
			else{
				$("#result").removeClass('hidden');
			}
		})
		.fail(function() {
			$('#login').html("Đăng nhập");
			alert("Đã có lỗi xảy ra! Vui lòng thử lại sau.");
		})

	});
});