document.addEventListener("DOMcontentLoaded", function() {
    //part 1
    //declaring
    const correct = document.QuerySelector("#correct");

    correct.addEventListener('click', function() {
        correct.style.backgroundColor = "green";
        document.QuerySelector('#correction').innerhtml = "correct";
    });
    //looping through class of incorrect answers
    for (let i = 0; i < incorrect.length; i++) {
        //declaring
        const incorrect = document.QuerySelectorALL(".incorrect");
        incorrect[i].addEventListener('click', function() {
            incorrect[i].style.backgroundColor = "red";
            document.QuerySelector('#correction').innerhtml = "incorrect";
        });
    }
    //part2
    document.QuerySelector("#check").addEventListener('click', function() {
        const input = QuerySelector("input");
        //if answer correct display correct
        if (input.value == "Mr. Darcy") {
            input.style.backgroundColor = "green";
            document.QuerySelector('#correction1').innerhtml = "correct";
        } //if not incorrect
        else {
            input.style.backgroundColor = "red";
            document.QuerySelector('#correction1').innerhtml = "incorrect";

        }
    });

});