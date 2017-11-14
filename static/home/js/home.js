// '.tbl-content' consumed little space for vertical scrollbar, scrollbar width depend on browser/os/platfrom. Here calculate the scollbar width .
$(window).on("load resize ", function() {
  var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
  $('.tbl-header').css({'padding-right':scrollWidth});

 
  $('#btnDone').click(function() {
  	swal({
	  title: 'Bạn đã hoàn thành công việc!',
	  text: "",
	  type: 'success',
	  showCancelButton: true,
	  confirmButtonColor: '#3085d6',
	  cancelButtonColor: '#d33',
	  confirmButtonText: 'HOÀN THÀNH',
	  cancelButtonText:'Hủy bỏ'
	}).then(function () {
	  swal(
	    'RẨT TỐT!',
	    'Xin chúc mừng bạn đã hoàn thành công việc!',
	    'success'
	  )
	})
  });
}).resize();