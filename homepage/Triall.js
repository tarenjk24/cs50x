document.addEventListener("DOMcontentLoaded", function() {

	document.QuerySelector("#check").addEventListener('click', function() {
		const input = QuerySelector("#code");
		//if answer correct display correct
		if (input.value == "Hello Mario") {
			input.style.backgroundColor = "green";
			document.QuerySelector('#correction').innerhtml = "correct";
		} //if not incorrect
		else {
			input.style.backgroundColor = "red";
			document.QuerySelector('#correction').innerhtml = "incorrect";

		}
	});
	document.QuerySelector("#check1").addEventListener('click', function() {
		const input = QuerySelector("#code1");
		//if answer correct display correct
		if (input.value == 10) {
			input.style.backgroundColor = "green";
			document.QuerySelector('#correction1').innerhtml = "correct";
		} //if not incorrect
		else {
			input.style.backgroundColor = "red";
			document.QuerySelector('#correction1').innerhtml = "incorrect";
		}
	});
	document.QuerySelector("#check2").addEventListener('click', function() {
		const input = QuerySelector("#code2");
		//if answer correct display correct
		if (input.value == 0) {
			input.style.backgroundColor = "green";
			document.QuerySelector('#correction2').innerhtml = "correct";
		} //if not incorrect
		else {
			input.style.backgroundColor = "red";
			document.QuerySelector('#correction2').innerhtml = "incorrect";
		}
	});
	document.QuerySelector("#check3").addEventListener('click', function() {
		const input = QuerySelector("#code3");
		//if answer correct display correct
		if (input.value == "This is the greater number 10") {
			input.style.backgroundColor = "green";
			document.QuerySelector('#correction3').innerhtml = "correct";
		} //if not incorrect
		else {
			input.style.backgroundColor = "red";
			document.QuerySelector('#correction3').innerhtml = "incorrect";
		}
	});
	document.QuerySelector("#check4").addEventListener('click', function() {
		const input = QuerySelector("#code4");
		//if answer correct display correct
		if (input.value == 110) {
			input.style.backgroundColor = "green";
			document.QuerySelector('#correction4').innerhtml = "correct";
		} //if not incorrect
		else {
			input.style.backgroundColor = "red";
			document.QuerySelector('#correction4').innerhtml = "incorrect";
		}
	});
});
