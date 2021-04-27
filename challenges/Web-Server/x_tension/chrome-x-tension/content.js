chrome.runtime.onMessage.addListener(
    function(message, sender, sendResponse) {

        switch(message.type) {
            case "enableExtension":
                redirectToDecodeurPage();
                break;

            case "disableExtension":
                redirecttoIndex();
                break;
        }
    }
);

// function encrypt(message = '', key = ''){
//     return CryptoJS.AES.encrypt(message, key).toString();
// }

function decrypt(message = '', key = ''){
    var code = CryptoJS.AES.decrypt(message, key);
    var decryptedMessage = code.toString(CryptoJS.enc.Utf8);
    return decryptedMessage;
}

AES_KEY = "PHACK{CRX_F1l3_R3v3rs1nG}"

document.addEventListener("uncipher_request", function(data) {
    unciphered = decrypt(document.getElementById('ciphered_text').value, AES_KEY);
    document.dispatchEvent(new CustomEvent('usEvent', {detail: unciphered}));
});

chrome.storage.sync.get("isEnabled", function(items) {
    if(items.isEnabled) {
        redirectToDecodeurPage();
    }
    else {
        redirecttoIndex();
    }
});

function redirectToDecodeurPage(){
  if ( !document.location.href.includes("256c936a-fe91-4263-8373-c82ad1549ef5")) {
    document.location = "/256c936a-fe91-4263-8373-c82ad1549ef5";
  }
}

function redirecttoIndex(){
  if ( document.location.href.includes("256c936a-fe91-4263-8373-c82ad1549ef5")) {
    document.location = "/";
  }
}
