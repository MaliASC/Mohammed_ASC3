var makerURL="https://maker.ifttt.com/trigger/OccuredAt/with/key/iuTN13qGWWm6siENXWIoNX1wstOlmnsVr6uGqhHel7E"



function submit(){

	var file = $("#resumeURL").val();
	//storing URL file in var sendoff
	var sendoff{
		"OccuredAt" : file;

	}
	// sends info to ITFFF.xom
	$.post(makerURL, sendoff);
}