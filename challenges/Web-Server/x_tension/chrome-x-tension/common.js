function getSavedValue(keyToGet, callback) {
	chrome.storage.sync.get(keyToGet, function(data) {
		callback(data[keyToGet]);
	});
}

function getAllSettings(callback) {
	chrome.storage.sync.get(null, function(items) {
	    callback(items);
	});
}

function saveValue(keyToSave, valueToSave) {
	chrome.storage.sync.set({ keyToSave: valueToSave });
}
