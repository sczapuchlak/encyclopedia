window.onload = function() {


    let search = document.querySelector('#term');
    search.addEventListener('keyup', keyPressed);
    let suggestions = document.querySelector('#predictive');
    let allWords = [
        'cat',
        'dog',
        'hippopotamus',
        'banana',
        'fruit',
        'hippopotamus',
    ];

    function keyPressed(event) {
        let currentSearch = event.currentTarget.value;
        clearSuggestions();
        if (currentSearch && currentSearch !== '') {
            let matches = allWords.filter(word => word.indexOf(currentSearch) > -1);
            for (let i = 0; i < matches.length; i++) {
                let container = document.createElement('span');
                container.setAttribute('class', 'search-suggestion');
                container.appendChild(document.createTextNode(matches[i]));
                container.addEventListener('click', selectSpan);
                suggestions.appendChild(container);
            }
        }
        if (!suggestions.firstChild) {
            suggestions.setAttribute('class', 'hidden');
        } else {
            suggestions.setAttribute('class', '');
        }
    }

    function selectSpan(event) {
        console.log('selectSpan');
        let selectedValue = event.currentTarget.innerHTML;
        console.log('selectedValue', selectedValue);
        search.value = selectedValue;
        clearSuggestions()
    }

    function clearSuggestions() {
        while (suggestions.firstChild) {
            suggestions.removeChild(suggestions.firstChild);
        }
        if (!suggestions.firstChild) {
            suggestions.setAttribute("class", "hidden");
        } else {
            suggestions.setAttribute("class", "");
        }
    }

    const cheetahMeow = new Audio();
    cheetahMeow.src = url("http://www.kessels.com/CatSounds/lion3.wav")
};