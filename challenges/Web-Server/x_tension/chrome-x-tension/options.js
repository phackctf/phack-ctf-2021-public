/**
	Add click event listener for activated option
**/
document.getElementById('onoffswitch').addEventListener('click', function(){
	  var isEnabled = document.getElementById('onoffswitch').checked;
	  chrome.storage.sync.set({ "onoffswitch": isEnabled });
}, false);


getSavedValue("onoffswitch", function(data){

	if (data == undefined) {
		data = true;
	}

	document.getElementById('onoffswitch').checked = data;
});
