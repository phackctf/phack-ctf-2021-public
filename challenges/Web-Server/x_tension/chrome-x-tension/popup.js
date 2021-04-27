/**
	Add Dom loaded event listener
**/
document.addEventListener('DOMContentLoaded', function(){
	chrome.storage.sync.get("isEnabled", function(items) {
		document.getElementById('onoffswitch').checked = items.isEnabled;
		manageExtensionState(items.isEnabled);
    });
}, false)


/**
	Add click event listener for switch
**/
document.getElementById('onoffswitch').addEventListener('click', function(){
	  var isEnabled = document.getElementById('onoffswitch').checked;
	  manageExtensionState(isEnabled);
}, false);


function manageExtensionState(isEnabled) {
	if (isEnabled) {
		chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
		    chrome.tabs.sendMessage(tabs[0].id, {type:"enableExtension"}, function(response){
		    });
		});
	}
	else {
		chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
		    chrome.tabs.sendMessage(tabs[0].id, {type:"disableExtension"}, function(response){
		    });
		});
	}

  chrome.storage.sync.set({'isEnabled': isEnabled}, function() {});
}


/**
	Add click event listener for option page opening
**/
document.getElementById('go-to-options').addEventListener('click', function(){
	  if (chrome.runtime.openOptionsPage) {
	    chrome.runtime.openOptionsPage();
	  }
	  else {
	    window.open(chrome.runtime.getURL('options.html'));
	  }
}, false);
