$(function () {
	var box = $(".chat01_content");

	box.scrollTop(box[0].scrollHeight+250);
    $(".ctb01").mouseover(function() {
			$(".wl_faces_box").show()
		}).mouseout(function() {
			$(".wl_faces_box").hide()
		}), $(".wl_faces_box").mouseover(function() {
			$(".wl_faces_box").show()
		}).mouseout(function() {
			$(".wl_faces_box").hide()
		}), $(".wl_faces_close").click(function() {
			$(".wl_faces_box").hide()
		}), $(".wl_faces_main img").click(function() {
			var a = $(this).attr("src");
			$("#textarea").val($("#textarea").val() + "*#" + a.substr(a.indexOf("img/") + 4, 6) + "#*"), $(".wl_faces_box").hide()
		})
})