/* 
	Initialize the lighbox on ever image with the marker css class "lightbox" 
*/
var items = document.querySelectorAll("img.lightbox");
items.forEach(function(item) {
	item.addEventListener("click", function(event) {
		console.log(event.target);
		const instance = basicLightbox.create('<img src="' + event.target.src + '" width="1024" height="768">');
		instance.show();
	});
});