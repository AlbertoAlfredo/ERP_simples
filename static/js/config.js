function setConfig(){
	var texts = {
		"title":"Aplicativo ERP"
	};
	document.title = texts.title;
	document.getElementById("navTitle").innerHTML = texts.title;
}

setConfig();